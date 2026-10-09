import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
s = open("ctl.pcb.toml").read()
s = re.sub(r"(?ms)^# plan (\w+)\n.*?^# end plan \1\n", "", s)
parts = re.split(r"(?m)^(?=\[\[)", s)
drop = ("[[tracks]]", "[[vias]]", "[[fills]]")
open("ctl.pcb.toml", "w").write("".join(b for b in parts if not b.startswith(drop)))
