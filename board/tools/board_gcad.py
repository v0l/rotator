import os, subprocess
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.XCAFDoc import XCAFDoc_DocumentTool
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.TDF import TDF_LabelSequence
from OCP.TDataStd import TDataStd_Name
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib

X0, Y0, ZB, T = -134.0, 14.0, 21.0, 1.6
TALL = 2.5
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STEP = os.path.join(REPO, "parts/vendor/ctl_board.step")
HOLES = [(4, 4), (84, 4), (4, 55.5), (84, 54)]
CANS = {"C2": 10.0, "C76": 8.0, "C83": 8.0}

subprocess.run(["agentee", "export", "ctl", "-o", STEP], cwd=os.path.join(REPO, "board"), check=True, stdout=subprocess.DEVNULL)
doc = TDocStd_Document(TCollection_ExtendedString("x"))
reader = STEPCAFControl_Reader()
reader.SetNameMode(True)
reader.ReadFile(STEP)
reader.Transfer(doc)
tool = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
roots = TDF_LabelSequence()
tool.GetFreeShapes(roots)
comps = TDF_LabelSequence()
tool.GetComponents_s(roots.Value(1), comps)


tall = []
for i in range(1, comps.Length() + 1):
    label = comps.Value(i)
    name = TDataStd_Name()
    ref = name.Get().ToExtString() if label.FindAttribute(TDataStd_Name.GetID_s(), name) else ""
    shape = tool.GetShape_s(label)
    box = Bnd_Box()
    BRepBndLib.Add_s(shape, box, True)
    x0, y0, z0, x1, y1, z1 = box.Get()
    if ref == "PCB" or z1 - T < TALL:
        continue
    tall.append((ref, x0, y0, max(z0, T), x1, y1, z1))

out = [
    "let zb=%g t=%g" % (ZB, T),
    "plane XY offset=zb",
    "rect 88 80 at=%g,%g r=1" % (X0 + 44, Y0 - 40),
    "board: extrude t",
    "plane board.end",
    "mount: hole 3.2 " + " ".join("%g,%g" % (X0 + x, Y0 - y) for x, y in HOLES),
    "color #1f6b3a",
    "material fr4 density=1.85",
]
for ref, x0, y0, z0, x1, y1, z1 in tall:
    r = ref.lower()
    cx, cy = X0 + (x0 + x1) / 2, Y0 + (y0 + y1) / 2
    out += ["body " + r, "plane XY offset=zb+t"]
    if ref in CANS:
        out += ["circle %g at=%.2f,%.2f" % (CANS[ref], cx, cy), "%s: extrude %.2f" % (r, z1 - T)]
    else:
        out += ["rect %.2f %.2f at=%.2f,%.2f" % (x1 - x0, y1 - y0, cx, cy), "%s: extrude %.2f" % (r, z1 - T)]
    out.append("combine main " + r)
open(os.path.join(REPO, "parts/ctl_board.gcad"), "w").write("\n".join(out) + "\n")
print(len(tall), "parts:", " ".join(t[0] for t in tall))
