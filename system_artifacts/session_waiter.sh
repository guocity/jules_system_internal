echo "${BASHPID}"
RUN_ROOT_DIR=/run/devbox-session/default
PANE_PID="1276"
# sleep 1  # enable this to mimic very slow command start.
# set -x
umask 0
sudo mkdir -m777 -p "${RUN_ROOT_DIR}"
coproc inw {
    LC_ALL=C exec inotifywait -e create,moved_to --include '/stamp$' "${RUN_ROOT_DIR}" 2>&1
}
set -m
(
    # If the pane has exited, also end the wait.
    if ps -p ${PANE_PID} > /dev/null; then
      tail --pid "${PANE_PID}" -f /dev/null
    fi
    touch "${RUN_ROOT_DIR}/stamp"
) &
pane_waiter=$!
echo "pane waiter is at $pane_waiter"
while IFS= read -r -u "${inw[0]}" line 2>/dev/null; do
    if [ "$line" = "Watches established." ]; then
        break
    fi
done
if [ -e "${RUN_ROOT_DIR}/stamp" ]; then
    echo "stamp found"
    kill "$inw_PID"
else
    echo "waiting for stamp"
    wait -n
fi
echo "done"
kill -- "-$pane_waiter" || exit 0
