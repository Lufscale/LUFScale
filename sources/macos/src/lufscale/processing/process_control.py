"""Contrôle thread-safe de l'annulation et de la pause des processus."""

from __future__ import annotations

import os
import signal
import subprocess
import threading
import time
from collections.abc import Callable

try:
    import psutil
except ImportError:
    psutil = None

_PROCESS_CONTROL_ERRORS: tuple[type[BaseException], ...] = (
    OSError,
    ProcessLookupError,
)
if psutil is not None:
    _PROCESS_CONTROL_ERRORS += (psutil.Error,)


class ProcessControl:
    """Centralise le cycle pause, reprise et annulation des sous-processus."""

    def __init__(
        self,
        cancellation_message: Callable[[], str],
        *,
        cancel_kill_grace_seconds: float = 1.0,
    ) -> None:
        self.cancellation_message = cancellation_message
        self.cancel_kill_grace_seconds = max(
            0.0, float(cancel_kill_grace_seconds)
        )
        self.cancel_event = threading.Event()
        self.pause_event = threading.Event()
        self.pause_condition = threading.Condition()
        self.process_lock = threading.Lock()
        self.current_processes: set[subprocess.Popen[str]] = set()
        self._pause_started_at: float | None = None
        self._paused_seconds = 0.0

    def register_process(self, process: subprocess.Popen[str]) -> bool:
        """Enregistre un processus et applique l'état déjà demandé.

        L'enregistrement a volontairement lieu avant la lecture de l'état :
        une pause ou une annulation concurrente voit ainsi toujours le
        processus, et une annulation antérieure est réappliquée dès son
        arrivée dans le registre.
        """
        with self.process_lock:
            self.current_processes.add(process)
        with self.pause_condition:
            cancelled = self.cancel_event.is_set()
            paused = self.pause_event.is_set()
        if cancelled:
            self._terminate_process(process)
            return False
        if paused:
            self.set_process_paused(process, True)
        return True

    def unregister_process(self, process: subprocess.Popen[str]) -> None:
        with self.process_lock:
            self.current_processes.discard(process)

    @staticmethod
    def _kill_if_running(process: subprocess.Popen[str]) -> None:
        if process.poll() is not None:
            return
        kill = getattr(process, "kill", None)
        if not callable(kill):
            return
        try:
            kill()
        except OSError:
            pass

    def _schedule_force_kill(self, process: subprocess.Popen[str]) -> None:
        grace = self.cancel_kill_grace_seconds
        if grace <= 0.0:
            self._kill_if_running(process)
            return

        def force_kill_after_grace() -> None:
            time.sleep(grace)
            self._kill_if_running(process)

        threading.Thread(
            target=force_kill_after_grace,
            name="lufscale-cancel-reaper",
            daemon=True,
        ).start()

    def _terminate_process(self, process: subprocess.Popen[str]) -> None:
        if process.poll() is not None:
            return
        # SIGTERM can remain pending on a stopped POSIX process.  Always send
        # the resume signal first, even if the presentation state has already
        # left Pause or a concurrent transition made that state stale.
        self.set_process_paused(process, False)
        try:
            process.terminate()
        except OSError:
            pass
        self._schedule_force_kill(process)

    @staticmethod
    def set_process_paused(
        process: subprocess.Popen[str], paused: bool
    ) -> None:
        if process.poll() is not None:
            return
        try:
            if os.name == "posix":
                process.send_signal(signal.SIGSTOP if paused else signal.SIGCONT)
            elif psutil is not None:
                managed = psutil.Process(process.pid)
                managed.suspend() if paused else managed.resume()
        except _PROCESS_CONTROL_ERRORS:
            pass

    def active_elapsed_since(self, started_at: float) -> float:
        now = time.perf_counter()
        with self.pause_condition:
            paused = self._paused_seconds
            if self._pause_started_at is not None:
                paused += now - self._pause_started_at
        return max(0.0, now - started_at - paused)

    def wait_if_paused(self) -> None:
        with self.pause_condition:
            while self.pause_event.is_set() and not self.cancel_event.is_set():
                self.pause_condition.wait(timeout=0.2)
        if self.cancel_event.is_set():
            raise InterruptedError(self.cancellation_message())

    def request_cancel(self) -> None:
        self.cancel_event.set()
        with self.pause_condition:
            if self._pause_started_at is not None:
                self._paused_seconds += time.perf_counter() - self._pause_started_at
                self._pause_started_at = None
            self.pause_event.clear()
            self.pause_condition.notify_all()
        with self.process_lock:
            processes = list(self.current_processes)
        for process in processes:
            self._terminate_process(process)

    def request_pause(self) -> bool:
        if self.cancel_event.is_set():
            return False
        with self.pause_condition:
            if self.pause_event.is_set():
                return False
            self.pause_event.set()
            self._pause_started_at = time.perf_counter()
        with self.process_lock:
            processes = list(self.current_processes)
        for process in processes:
            self.set_process_paused(process, True)
        return True

    def request_resume(self) -> bool:
        with self.pause_condition:
            if not self.pause_event.is_set():
                return False
            if self._pause_started_at is not None:
                self._paused_seconds += time.perf_counter() - self._pause_started_at
                self._pause_started_at = None
            self.pause_event.clear()
            self.pause_condition.notify_all()
        with self.process_lock:
            processes = list(self.current_processes)
        for process in processes:
            self.set_process_paused(process, False)
        return True


__all__ = ["ProcessControl"]
