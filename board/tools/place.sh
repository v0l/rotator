#!/bin/sh
set -e
cd "$(dirname "$0")/.."
python3 tools/strip_copper.py
python3 tools/unplace_unlocked.py
agentee edit pcb ctl tools/place_fixed.txt > /dev/null 2>&1 || true
python3 tools/unplace_unlocked.py
agentee edit pcb ctl tools/driver_routes.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/poe_routes.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/eth_routes.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/misc_routes.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/keeper_place.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/keeper_routes.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/poe_vias.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/v24_vias.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/c2_route.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/gnd_vias.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/buck_place.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/buck_routes.txt > /dev/null 2>&1 || true
agentee edit pcb ctl tools/usb_routes.txt > /dev/null 2>&1 || true
agentee place ctl --keep-placed > /dev/null
python3 tools/strip_passives.py
agentee place ctl --keep-placed --side both | python3 -c "import json,sys; print(json.load(sys.stdin)['result'])"
