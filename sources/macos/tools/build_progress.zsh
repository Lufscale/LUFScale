# Optional worker milestones; the outer supervisor owns the display and log.
build_stage() {
    if [[ -n "${LUFSCALE_PROGRESS_FILE:-}" ]]; then
        printf '%s|%s\n' "$1" "$2" > "${LUFSCALE_PROGRESS_FILE}.tmp"
        /bin/mv -f -- "${LUFSCALE_PROGRESS_FILE}.tmp" "$LUFSCALE_PROGRESS_FILE"
    fi
}
