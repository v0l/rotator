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

The az bearings are 49 mm apart and the load is 213 mm above the lower one, so the upper
bearing carries 620 N and the lower 475 N.

| sim | what it models | result |
|---|---|---|
| `spindle` | Ø15 silver steel az spindle, bearings, wheel keyway, collar | 80 MPa above the upper bearing, 155 MPa peak at the keyway corner, safety 2.6 |
| `elshaft` | Ø15 el shaft, bush contact at each crossboom end | 87 MPa at the bearing, 28 MPa at the cross hole, safety 4.6 at the bearing |
| `elbox` | el box body on the collar, gusty-side bearing loads | under 10 MPa in the die-cast walls; the box top moves 0.34 mm |
| `azframe` | mast clamp, box floor, three posts and the bearing plate | posts 28 MPa, floor 13 MPa, clamp 4 MPa; bearing plate moves 0.1 mm |

Peak stresses printed at fixed-face edges and bonded joints are mesh singularities; the
`expect` lines check probes away from them.

What this changed:

- The three posts were M6 brass, 10 mm hex. They had about 10 N·m at each base and the
  brass ran close to yield, so they are now M8 stainless, 13 mm hex, 70 mm long.
- The mast clamp flange is lightly stressed; the floor of the az box is too.

Not covered here: the worm wheels. The gusty-side 16.6 N·m on the az wheel is more than
the 7.4 N·m KHK lists for CG1-60R1 at 100 rpm, which is a wear rating. Check the static
bending rating before trusting the gears in a storm.
