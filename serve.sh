#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="${SCRIPT_DIR}"
DECK_PATH="/presentation.html"

PREFERRED_PORT="8001"
NO_OPEN="0"

for arg in "$@"; do
  if [[ "${arg}" == "--no-open" ]]; then
    NO_OPEN="1"
  elif [[ "${arg}" =~ ^[0-9]+$ ]]; then
    PREFERRED_PORT="${arg}"
  else
    echo "Usage: $(basename "$0") [port] [--no-open]" >&2
    exit 2
  fi
done

PYTHON_BIN=""
if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Error: python not found (need python3)." >&2
  exit 1
fi

is_port_free() {
  local port="$1"
  if command -v lsof >/dev/null 2>&1; then
    ! lsof -nP -iTCP:"${port}" -sTCP:LISTEN >/dev/null 2>&1
    return
  fi

  "${PYTHON_BIN}" - "${port}" <<'PY'
import socket, sys
port = int(sys.argv[1])
for host in ("127.0.0.1", "::1"):
  try:
    family = socket.AF_INET6 if ":" in host else socket.AF_INET
    s = socket.socket(family, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
  except OSError:
    sys.exit(1)
  finally:
    try:
      s.close()
    except Exception:
      pass
sys.exit(0)
PY
}

PORT=""
for ((n=0; n<50; n++)); do
  candidate=$((PREFERRED_PORT + n))
  if is_port_free "${candidate}"; then
    PORT="${candidate}"
    break
  fi
done

if [[ -z "${PORT}" ]]; then
  echo "Error: couldn't find a free port starting at ${PREFERRED_PORT}." >&2
  exit 1
fi

URL="http://localhost:${PORT}${DECK_PATH}"

echo "Serving from: ${REPO_ROOT}"
echo "Deck URL: ${URL}"
echo
echo "Press Ctrl+C to stop."

if [[ "${NO_OPEN}" != "1" ]]; then
  if command -v open >/dev/null 2>&1; then
    open "${URL}" || true
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "${URL}" >/dev/null 2>&1 || true
  fi
fi

exec "${PYTHON_BIN}" -m http.server "${PORT}" --directory "${REPO_ROOT}"
