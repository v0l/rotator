import re
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")

ag_sym = '''name = "Ag5424"
reference = "U"
value = "Ag5424"
description = "Silvertel Ag5400 PoE+ PD module, IEEE 802.3at class 4, 24 V 1.25 A isolated output, SIL"
datasheet = "https://silvertel.com/images/datasheets/Ag5400-datasheet-high%20Efficiency-30W-Power-Over-Ethernet-Plus-Module-PoE+PD.pdf"
footprint = "Silvertel_Ag5400_SIL"

[[bodies]]
width = 20.32
left = [
  { number = "1", name = "VIN+", type = "power_in" },
  { number = "2", name = "VIN-", type = "power_in" },
  { number = "3", name = "AT-DET", type = "open_collector" },
  { gap = 1 },
  { number = "4", name = "IC", type = "no_connect" },
  { number = "5", name = "IC", type = "no_connect" },
  { number = "6", name = "IC", type = "no_connect" },
]
right = [
  { number = "8", name = "+VDC", type = "power_out" },
  { number = "9", name = "ADJ", type = "passive" },
  { gap = 1 },
  { number = "7", name = "-VDC", type = "power_out" },
  { number = "10", name = "-VDC", type = "passive" },
]
'''
open("symbols/Ag5424.sym.toml", "w").write(ag_sym)

xs = [0, 2.54, 5.08, 7.62, 10.16, 12.7, 43.18, 45.72, 48.26, 50.8]
ag = '''name = "Silvertel_Ag5400_SIL"
description = "Silvertel Ag5400 PoE module, single in line, 10 pins at 2.54 mm in two groups 30.48 mm apart, 1.1 mm holes, component keep-out from datasheet V1.3 figure 14: 62 mm long, 6 mm from the card on the -y side (pins 9 mm in), 5, 13.5 and 7 mm on the +y side over 23.9, 18 and 15.4 mm with the transformer in the middle section"
tags = ["PoE", "Silvertel"]
mount = "tht"
height = "14mm"
model = "models/Ag5400_simplified.step"
model_rotate = [-90, 0, 0]
model_offset = ["0mm", "2.87mm", "1.27mm"]

'''
for i, x in enumerate(xs):
    ag += '[[pads]]\nnumber = "%d"\nkind = "tht"\nshape = "%s"\nat = [%.2f, 0]\nsize = [1.8, 1.8]\ndrill = 1.1\n%s\n' % (i + 1, "rect" if i == 0 else "circle", x, 'zone_connect = "solid"\n' if i + 1 in (7, 8, 10) else "")
x0, x1 = -5.11, 52.19
xa, xb = x0 + 23.9, x0 + 23.9 + 18
card = -9.0 + 7.6
body = [[x0, -9.0], [x1, -9.0], [x1, card + 7], [xb, card + 7], [xb, card + 13.5], [xa, card + 13.5], [xa, card + 5], [x0, card + 5]]
keep = [[x0 - 2.35, -9.0], [x1 + 2.35, -9.0], [x1 + 2.35, card + 7], [xb, card + 7], [xb, card + 13.5], [xa, card + 13.5], [xa, card + 5], [x0 - 2.35, card + 5]]
for layer, pts, wd in (("F.Fab", body, "0.1"), ("F.SilkS", body, "0.15"), ("F.CrtYd", keep, "0.05")):
    ag += '[[graphics]]\nkind = "polygon"\nlayer = "%s"\npoints = [%s]\nwidth = %s\n\n' % (layer, ", ".join("[%.2f, %.2f]" % (x, y) for x, y in pts), wd)
ag += '[[graphics]]\nkind = "text"\nlayer = "F.SilkS"\ntext = "${REFERENCE}"\nat = [25, 6]\nsize = 1.0\n'
open("footprints/Silvertel_Ag5400_SIL.fp.toml", "w").write(ag)

IN = 25.4
def tht(num, x, y, drill, size, shape="circle"):
    return '[[pads]]\nnumber = "%s"\nkind = "tht"\nshape = "%s"\nat = [%.3f, %.3f]\nsize = [%.2f, %.2f]\ndrill = %.2f\n\n' % (num, shape, x * IN, y * IN, size, size, drill)

v8_sym = '''name = "V8BR-1AX1-GH"
reference = "J"
value = "V8BR-1AX1-GH"
description = "Bel gigabit MagJack, vertical (top entry), 4PPoE 600 mA per pair, -40 to 85 C, centre taps of all four pairs out, two LEDs; drawing V8BR-1AX1-GH rev PC"
datasheet = "https://www.belfuse.com/media/drawings/products/magjack%20ICMs/dr-mag-v8br-1ax1-gh.pdf"
footprint = "RJ45_Bel_V8BR-1AX1-GH_Vertical"

[[bodies]]
width = 25.4
left = [
  { number = "11", name = "TRD1+", type = "passive" },
  { number = "12", name = "TRCT1", type = "passive" },
  { number = "10", name = "TRD1-", type = "passive" },
  { number = "4", name = "TRD2+", type = "passive" },
  { number = "6", name = "TRCT2", type = "passive" },
  { number = "5", name = "TRD2-", type = "passive" },
  { number = "3", name = "TRD3+", type = "passive" },
  { number = "1", name = "TRCT3", type = "passive" },
  { number = "2", name = "TRD3-", type = "passive" },
  { number = "8", name = "TRD4+", type = "passive" },
  { number = "7", name = "TRCT4", type = "passive" },
  { number = "9", name = "TRD4-", type = "passive" },
  { gap = 1 },
  { number = "18", name = "LEDY_A", type = "passive" },
  { number = "17", name = "LEDY_K", type = "passive" },
  { number = "20", name = "LEDG_A", type = "passive" },
  { number = "19", name = "LEDG_K", type = "passive" },
]
right = [
  { number = "13", name = "VC12", type = "passive" },
  { number = "14", name = "VC36", type = "passive" },
  { number = "15", name = "VC45", type = "passive" },
  { number = "16", name = "VC78", type = "passive" },
  { gap = 6 },
  { number = "SH", name = "SHIELD", type = "passive" },
]
'''
open("symbols/V8BR-1AX1-GH.sym.toml", "w").write(v8_sym)

v8 = '''name = "RJ45_Bel_V8BR-1AX1-GH_Vertical"
description = "Bel V8BR-1AX1-GH vertical MagJack, through hole; origin on the board lock line, pins toward +y (drawing V8BR-1AX1-GH rev PC, page 4)"
tags = ["RJ45", "MagJack", "PoE", "vertical"]
mount = "tht"
height = "17mm"
clearance = "0.1mm"
model = "models/V8BR-1AX1-GH.stp"
model_offset = ["0mm", "-4.953mm", "16.79mm"]

'''
sig = {"1": (0.200, 0.295), "3": (0.120, 0.295), "5": (0.040, 0.295), "7": (-0.040, 0.295), "9": (-0.120, 0.295), "11": (-0.200, 0.295),
       "2": (0.160, 0.354), "4": (0.080, 0.354), "6": (0.0, 0.354), "8": (-0.080, 0.354), "10": (-0.160, 0.354), "12": (-0.240, 0.354),
       "13": (0.288, 0.078), "14": (0.288, 0.158), "15": (-0.288, 0.078), "16": (-0.288, 0.158)}
for num, (x, y) in sig.items():
    v8 += tht(num, x, y, 0.95, 1.35)
for num, x in (("17", 0.257), ("18", 0.157), ("19", -0.157), ("20", -0.257)):
    v8 += tht(num, x, -0.138, 1.1, 1.6)
for x in (-0.354, 0.354):
    v8 += tht("SH", x, 0.354, 1.6, 2.4)
for x in (-0.197, 0.197):
    v8 += '[[pads]]\nnumber = ""\nkind = "npth"\nshape = "circle"\nat = [%.3f, 0]\nsize = [3.25, 3.25]\ndrill = 3.25\n\n' % (x * IN)
bw, by0, by1 = 9.3, -5.23, 15.42
for layer, w, m, wd in (("F.Fab", bw, 0, "0.1"), ("F.SilkS", 10.3, 0, "0.15"), ("F.CrtYd", 10.3, 0.4, "0.05")):
    v8 += '[[graphics]]\nkind = "rect"\nlayer = "%s"\nstart = [%.2f, %.2f]\nend = [%.2f, %.2f]\nwidth = %s\n\n' % (layer, -w - m, by0 - m, w + m, by1 + m, wd)
v8 += '[[graphics]]\nkind = "text"\nlayer = "F.SilkS"\ntext = "${REFERENCE}"\nat = [0, %.2f]\nsize = 1.0\n' % (by1 + 1.6)
open("footprints/RJ45_Bel_V8BR-1AX1-GH_Vertical.fp.toml", "w").write(v8)

br_sym = open("symbols/MBL106S.sym.toml").read().split("\n", 1)[1]
br_sym = br_sym.replace('name = "MBL106S"', 'name = "CDBHM2100L-G"', 1)
br_sym = br_sym.replace(
    'description = "Miniature Glass Passivated Single-Phase Surface Mount Bridge Rectifiers, 420V Vrms, 1.0A If, MBLS SMD package"',
    'description = "Comchip CDBHM2100L-G low VF Schottky bridge rectifier, 100 V, 2 A, VF 0.85 V max at 2 A, MBS-2 case"',
)
br_sym = br_sym.replace('datasheet = "http://www.vishay.com/docs/89959/mbl104s.pdf"', 'datasheet = "https://www.comchiptech.com/admin/files/product/CDBHM220L-G%20Thru.%20CDBHM2100L-G%20RevB.pdf"')
br_sym = re.sub(r'(?m)^footprint = ".*"$', 'footprint = "Diode_Bridge_MBS-2"', br_sym)
br_sym = br_sym.replace('footprint_filters = ["Diode*Bridge*Vishay*MBLS*"]', 'footprint_filters = ["Diode*Bridge*MBS*"]')
open("symbols/CDBHM2100L-G.sym.toml", "w").write(br_sym)

br = '''name = "Diode_Bridge_MBS-2"
description = "MBS-2 (TO-269AA) bridge rectifier, 4.7 x 4.0 x 2.7 mm body, 2.55 mm pitch, 7.0 mm max over the leads, + and - on the -x side (Comchip CDBHM2100L-G RevB)"
tags = ["bridge", "MBS"]
mount = "smd"
height = "2.7mm"

'''
for num, x, y in (("1", -2.85, -1.275), ("2", 2.85, -1.275), ("3", 2.85, 1.275), ("4", -2.85, 1.275)):
    br += '[[pads]]\nnumber = "%s"\nkind = "smd"\nshape = "rect"\nat = [%.3f, %.3f]\nsize = [1.3, 1.0]\nlayers = ["F.Cu", "F.Mask", "F.Paste"]\n\n' % (num, x, y)
for layer, hx, hy, wd in (("F.Fab", 2.0, 2.35, "0.1"), ("F.CrtYd", 3.75, 2.6, "0.05")):
    br += '[[graphics]]\nkind = "rect"\nlayer = "%s"\nstart = [%.3f, %.3f]\nend = [%.3f, %.3f]\nwidth = %s\n\n' % (layer, -hx, -hy, hx, hy, wd)
for a, b in (((-1.5, -2.5), (1.5, -2.5)), ((-1.5, 2.5), (1.5, 2.5))):
    br += '[[graphics]]\nkind = "line"\nlayer = "F.SilkS"\nstart = [%.2f, %.2f]\nend = [%.2f, %.2f]\nwidth = 0.15\n\n' % (a + b)
br += '[[graphics]]\nkind = "text"\nlayer = "F.SilkS"\ntext = "+"\nat = [-1.4, -1.275]\nsize = 1.0\n\n'
br += '[[graphics]]\nkind = "text"\nlayer = "F.SilkS"\ntext = "${REFERENCE}"\nat = [0, -3.4]\nsize = 1.0\n'
open("footprints/Diode_Bridge_MBS-2.fp.toml", "w").write(br)
