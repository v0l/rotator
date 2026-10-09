import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
big = {"C1", "C2", "C76", "C83"}
s = open("ctl.pcb.toml").read()
parts = re.split(r"(?m)^(?=\[\[)", s)
def passive(b):
    if not b.startswith("[[footprints]]") or "locked = true" in b:
        return False
    r = re.search(r'ref = "([^"]+)"', b).group(1)
    return bool(re.match(r"^(R|FB)\d+$", r) or (re.match(r"^C\d+$", r) and r not in big))
open("ctl.pcb.toml", "w").write("".join(b for b in parts if not passive(b)))
