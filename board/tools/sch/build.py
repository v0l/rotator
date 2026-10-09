import re, subprocess, sys
POWER = {"GND", "3V3", "V24", "VBUCK", "VDD_HP", "VDDO_FLASH", "VDDO_PSRAM", "VKEEP", "VBUS", "VDDA", "VCELL", "VBOOST"}
def build(sheet):
    lines = open(f"tools/sch/{sheet}.txt").read().splitlines()
    adds = [l for l in lines if l.startswith("add ")]
    rest = [l for l in lines if not l.startswith("add ")]
    out = []
    big_x, small_i = 25.4, 0
    for l in adds:
        ref = l.split()[1]
        if re.match(r"(U|J|BT)\d", ref):
            out.append(f"{l} --at {big_x:.2f},50.8")
            big_x += 76.2
        else:
            col, row = small_i % 16, small_i // 16
            out.append(f"{l} --at {25.4 + col * 15.24:.2f},{165.1 + row * 20.32:.2f}")
            small_i += 1
    for l in rest:
        if l.startswith("net "):
            name = l.split()[1]
            l = re.sub(r" --sheet \S+", "", l) + f" --sheet {sheet} --style " + ("power" if name in POWER else "label")
        out.append(l)
    hdr = open(f"{sheet}.sch.toml").read().split("[[parts]]")[0].split("[[nets]]")[0]
    hdr = "\n".join(l for l in hdr.splitlines() if not l.startswith("no_connect")).rstrip() + "\n"
    open(f"{sheet}.sch.toml", "w").write(hdr)
    r = subprocess.run(["agentee", "edit", "sch", sheet, "-"], input="\n".join(out) + "\n", capture_output=True, text=True)
    print("\n".join((r.stdout + r.stderr).splitlines()[-6:]))
for s in sys.argv[1:]:
    build(s)
