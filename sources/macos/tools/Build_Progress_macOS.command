#!/bin/zsh
# UI-only supervisor: build output stays in a log; milestones come from workers.
set -u
cd -- "$(dirname -- "$0")/.."
mkdir -p build-logs
run_name="build-$(date +%Y%m%d-%H%M%S)-$$"
log_file="$PWD/build-logs/$run_name.log"
export LUFSCALE_PROGRESS_FILE="$PWD/build-logs/$run_name.progress"
export LUFSCALE_PROGRESS_WORKER=1
export LUFSCALE_DETAIL_FILE="$PWD/build-logs/$run_name.detail"
export PYTHONUNBUFFERED=1
printf '0|Preparing\n' > "$LUFSCALE_PROGRESS_FILE"

stop_tree() {
    local parent="$1" descendant
    for descendant in $(/usr/bin/pgrep -P "$parent" 2>/dev/null); do
        stop_tree "$descendant"
    done
    kill -TERM "$parent" 2>/dev/null || true
}

printf 'LUFScale 2.2.3 — macOS build\n'
printf 'One progress bar per stage; animation indicates recent build activity.\n'
printf 'No new messages does not necessarily mean the build is stalled.\n'
printf 'If macOS opens the Apple developer tools installer, complete it to continue.\n'
printf 'Full log: %s\n\n' "$log_file"
/bin/zsh ./Create_Community_Distribution_macOS.command > "$log_file" 2>&1 &
worker_pid=$!
trap 'stop_tree "$worker_pid"; printf "\nBuild cancelled. Log: %s\n" "$log_file"; exit 130' INT TERM HUP
started=$SECONDS
stage_started=$SECONDS
last_output=$SECONDS
last_size=0
shown=-1
titles=("Apple developer tools" "Preparing Python" "Dependencies" "PDF guides" "Building and validating FFmpeg" "Building LUFScale.app" "Validation and signing" "ZIP and checksums")
show_stages() {
    local target="$1"
    while (( shown < target && shown < 7 )); do
        if (( shown >= 0 )); then
            printf '\r\033[K[====================] Complete\n'
        fi
        (( shown += 1 ))
        printf '\nStage %s/8 — %s\n' "$((shown+1))" "${titles[$((shown+1))]}"
        stage_started=$SECONDS
    done
}
while kill -0 "$worker_pid" 2>/dev/null; do
    milestone=0
    label="Preparing"
    IFS='|' read -r milestone label < "$LUFSCALE_PROGRESS_FILE" || true
    case "$milestone" in [0-8]) ;; *) milestone=0 ;; esac
    # A worker milestone is published only after the preceding stage succeeds.
    target=$milestone
    (( target > 7 )) && target=7
    show_stages "$target"
    size=$(wc -c < "$log_file")
    if (( size != last_size )); then
        last_output=$SECONDS
        last_size=$size
    fi
    silent=$((SECONDS-last_output))
    detail="$label"
    if [[ -s "$LUFSCALE_DETAIL_FILE" && $milestone == 4 ]]; then
        detail=$(< "$LUFSCALE_DETAIL_FILE")
    fi
    max_detail=$(( ${COLUMNS:-80} - 1 ))
    (( max_detail < 20 )) && max_detail=20
    detail="${detail[1,$max_detail]}"
    bar="...................."
    if (( silent <= 2 )); then
        position=$(( (SECONDS-started) % 20 + 1 ))
        bar[$position]="="
        activity="Activity detected"
    else
        activity="No new messages for ${silent}s"
    fi
    printf '\r\033[K[%s] %ss — %s\n' "$bar" "$((SECONDS-stage_started))" "$activity"
    printf '\033[K%s' "$detail"
    sleep 1
    # Remove only the live detail row; completed stages remain above it.
    printf '\r\033[K\033[1A'
done
wait "$worker_pid"
result=$?
trap - INT TERM HUP
if (( result == 0 )); then
    show_stages 7
    printf '\r\033[K[====================] Complete\n\n8/8 — Build complete.\n'
    printf 'Application : %s/dist/LUFScale.app\n' "$PWD"
else
    printf '\r\033[K[!!!!!!!!!!!!!!!!!!!!] FAILED (code %s). Full log: %s\n' "$result" "$log_file"
    printf 'Last log messages:\n'
    tail -n 12 "$log_file"
fi
exit "$result"
