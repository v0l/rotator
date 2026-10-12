# Strength

Static FEA in gcad, `gcad sim NAME.gsim`, one load case: survival wind of 120 km/h
(q = 680 Pa) on two small satellite yagis.

| input | value |
|---|---|
| Drag per side, antenna plus crossboom | Cd·A = 0.095 m², 65 N, at 500 mm from the az axis |
| Antenna weight per side | 10 N |
| Head weight | 5 kg |
| Wind on the el box | 15 N |
| Gusty side | one antenna takes full wind, the other half, so the az axis sees 16.6 N·m |
| Horizontal load at the el axis | 144 N, 226 mm above the az box floor |
| Worm on the az wheel | 553 N at the 30 mm pitch radius, 32 mm above the floor |

## Bearings

KFL002: a K002 insert (15 x 32 mm, outer ring 9 wide, inner ring 16.5) in a two-bolt
zinc die-cast flange. Ratings from Mädler (62661500) and AMI: C = 5.7 kN, C0 = 2.9 kN;
Mädler gives these as the unit's maximum radial load, axial about 20% of that. The ball row
sits 4.5 mm from the short end of the inner ring (AMI `n`), which is 6.6 mm from the
flange's mounting face (Z - Bi + n). Datasheets are in `board/ref/maedler_*.pdf` and
`board/ref/kfl000_silver.pdf`.

| bearing | ball row | worst radial load | C0 / P0 |
|---|---|---|---|
| az upper | z 66.4 | 768 N (wind 549 N plus worm 218 N in line) | 3.8 |
| az lower | z 9.6 | 740 N (wind 405 N against worm 335 N) | 3.9 |
| el, wind side | x 33.1 | 222 N | 13 |
| el, lee side | x -62.6 | 125 N | 23 |

The az pair is 56.8 mm apart. Axial load is the head's weight, about 60 N, a tenth of the
axial limit.

## Sims

| sim | what it models | result |
|---|---|---|
| `kfl` | KFL002 zinc housing, bolt holes held, mounting face on the plate, 768 N on the ring seat plus 60 N axial | 2.5 MPa in the boss, 4.3 MPa at the flange root, 13 MPa peak; seat moves 2 µm. `--set ang=0` loads it along the bolt line: lower still |
| `spindle` | Ø15 silver steel az spindle pinned at the ball rows, wind at the el axis, az torque, worm force on the keyway | 80 MPa above the upper bearing, 73 MPa below the collar, 50 MPa at the keyway end |
| `elshaft` | Ø15 el shaft pinned at the ball rows, bush contact at each crossboom end | 87 MPa at the bearing, 28 MPa at the cross hole |
| `elbox` | el box body on the collar, gusty-side bearing loads | under 10 MPa in the die-cast walls; the box top moves 0.37 mm |
| `torque` | gravity plus the 120 km/h wind torques on both joints, worm losses from `lead=3.583 friction=mu`, el swept -6 to 186 | at friction 0.1: az motor 0.39 N·m, el motor 0.03 N·m, both worms lock; gravity alone is 0.18 N·m on el |

Peaks printed at fixed-face edges and at the ends of the pinned bands are mesh
singularities; the `expect` lines check probes away from them. A `pin` on a 2 mm band
still holds some moment, so the pinned reactions are skewed; the bearing loads above are
from statics.

Everything here is one body. The bearing, the shaft and the housing should be one bonded
assembly, but gcad's bonded joints leak moment: a shaft bonded into a bore and loaded at the
far end reports half the root moment and half the deflection of the same shape as one solid
(see `~/git/gcad/TODO.md`). The az frame sim (clamp, floor, posts, bearing plate) was bonded
too, so it was removed. By hand: the bearing plate on four posts is a portal frame, so each
post sees 192 N and 6.7 N·m at each end. An A2-70 M8 standoff preloaded to about 11 kN holds
that on its 13 mm shoulder with a wide margin.

## What this changed

- The bearing plate posts were M6 brass. They are M8 stainless, 13 mm hex, 70 mm long,
  four of them.

## Drive torque in wind

Wind at 120 km/h with the yagi pointing up and the wind across the crossboom. By hand: the yagi
takes about 22 N (boom 15 N at Cd 1.2, elements 5 N, clamp 2 N) at 300 mm from the az axis, and
the two crossboom tubes nearly cancel, so az sees about 6.3 N·m. The 9 mm `wind` run reads
8.9 N·m, high because the 4 mm elements are thinner than a cell. El sees under 0.5 N·m.

`torque.gsim` puts 8.9 N·m on az and 0.5 N·m on el and carries them through the worms with
their 3.583° lead. The mesh friction is the unknown, so it is a variable,
`gcad sim torque.gsim --set mu=0.15`:

| mesh friction | worm efficiency | az motor torque | el motor torque | back-drives |
|---|---|---|---|---|
| 0.05 (greased, running) | 0.55 | 0.27 N·m | 0.02 N·m | yes, 0.03 N·m at the az motor |
| 0.10 | 0.38 | 0.39 N·m | 0.03 N·m | no, locks |
| 0.15 (from rest) | 0.29 | 0.51 N·m | 0.04 N·m | no, locks |

The motor holds 0.45 N·m. It holds the head in any of these, since the worm locks above 0.063
and back-driving takes 7% of the motor at 0.05. Driving az starts to stall from rest at
120 km/h with the 8.9 N·m reading; with the 6.3 N·m hand figure it needs 0.36 N·m there. Park
above about 80 km/h.

## Open

The gusty-side 16.6 N·m on the az wheel is more than the 7.4 N·m KHK lists for CG1-60R1
at 100 rpm, which is a wear rating. Check the static bending rating before trusting the
gears in a storm.
