# Strength

Static FEA in gcad, `gcad sim NAME.gsim`, one load case: survival wind of 120 km/h
(q = 680 Pa) on the yagi, held by the locked worms.

| input | value |
|---|---|
| Drag on the yagi and its boom | Cd·A = 0.095 m², 65 N, 300 mm out along the bracket tube |
| Yagi, clamp and tube weight | 2 kg at the yagi |
| Head weight | 4 kg |
| Wind on the el box | 11 N |
| Az torque | 65 N at 273 mm, 17.6 N·m on the az wheel |
| El torque | 6.4 N·m on the el wheel |

## Bearings

| bearing | unit | worst radial load | static safety |
|---|---|---|---|
| az, inside the top wall | KFL003, C0 3.28 kN | 1223 N | 2.7 |
| az, outside the top wall | KFL003 | 706 N | 4.7 |
| el, lid | KFL001 | 416 N | |
| el, floor | KFL001 | 176 N | |

The az pair is 25.5 mm apart on one wall and the wheel hangs about 22 mm below the inner one,
so the worm's 580 N tooth force loads the inner bearing most.

## Sims

| sim | what it models | result |
|---|---|---|
| `azdrive` | `azstage.gasm`: the spindle in both KFL003 inserts as gcad bearings, wheel and collar on their dowels, worm in frictionless contact with the wheel at mesh 3 (14 contact solves, about 10 minutes), the drive held at its four hang holes, the motor end on a slide; head side load, overturning moment and 17.6 N·m on the collar's bolt holes | KFL003 loads 1223 N (inner) and 706 N (outer); 674 N and 19 N·m into the drive hangers; 390 N worm thrust into the motor end. Stresses at mesh 3 are not trusted; `spindle_tube` checks the spindle |
| `spindle_tube` | 17 x 2 az spindle alone, 42CrMo4+QT, ball rows as bearings, wheel dowel held, head loads on the collar | 48 to 54 MPa along the tube, 198 MPa at the collar dowel hole (safety 3.3) |
| `kfl` | KFL002 housing (smaller than the KFL003, so conservative) in aluminium, bolt holes held, 1223 N on the seat plus 27 N axial | 4 MPa in the hub, 7 MPa at the flange root, 17 MPa peak (safety 8.9) |
| `yoke` | the 3 mm darted yoke, both hubs and their clinch-nut holes held, the yagi's side force and weight at 300 mm put on the clamp holes as force and moments | 119 MPa peak at the tip of a dart's leg (safety 1.6), 0.25 mm at the crossbar; the hubs pass 11.0 and 17.4 N·m into the shaft, because the shaft locks the two arms together |
| `elshaft` | Ø12 el shaft on its KFL001 ball rows, the hub loads from `yoke` on each keyed end, the worm holding the wheel keyway plus its 97 N separating force | 57 MPa at the floor bearing, 92 MPa at the lid bearing, 99 MPa at the right hub, 107 MPa by the wheel key; 341 MPa at the square end of the wheel keyway, which a milled keyway end rounds off |
| `elbox` | 1550Z117 box and lid, held at the collar holes, the bearing and worm reactions from `elshaft` on the KFL and drive holes | 18 MPa peak by the collar holes (safety 8.8), 0.05 mm |
| `torque` | gravity plus wind torque on both joints at `kmh` (90 unless set, 8.9 N·m at 120 km/h scaled with speed squared), worm losses at friction `mu` (0.15, cold grease), the KHK mesh geometry, bearing and seal drag on every joint, both worms at 60 rpm, el swept -6 to 120 | az motor 0.33 N·m against the 0.36 the TMC2209 gets from it, el 0.15 N·m, both worms lock |

Peaks printed at fixed-face edges and sharp inside corners are mesh singularities; the
`expect` lines check probes away from them.

## Drive torque in wind

Wind at 120 km/h with the yagi pointing up. By hand: the yagi takes about 22 N (boom 15 N at Cd
1.2, elements 5 N, clamp 2 N) at 300 mm from the az axis, so az sees about 6.3 N·m. The 9 mm `wind` run reads
8.9 N·m, high because the 4 mm elements are thinner than a cell. El sees under 0.5 N·m.

`torque.gsim` puts 8.9 N·m on az and 0.5 N·m on el and carries them through the worms with
their 3.583° lead. Every other friction in the drive is a `drag=` on its joint, from the SKF
friction model (seal moment K_S1·d_s^β + K_S2 per seal, rolling 0.5·μ·P·d):

| joint | what drags | drag |
|---|---|---|
| `az` | two KFL003 inserts, both sides sealed, about 0.06 N·m each; rolling under the worst bearing loads (1223 N and 706 N, μ 0.0015, 17 mm), 0.02 N·m | 0.16 N·m (`daz`) |
| `el` | two KFL001 inserts, about 0.06 N·m each; rolling, under 0.02 N·m | 0.14 N·m (`del`) |
| `base.drive.spin`, `head.drive.spin` | two 608-2RSH, 0.011 N·m each; one taking the worm's 300 N thrust at μ 0.004, 0.005 N·m | 0.03 N·m (`dw`) |

Grease churn at a few degrees a
second is too small to count. The mesh friction is the unknown, so it is a variable,
`gcad sim torque.gsim --set mu=0.15`:

| mesh friction | worm efficiency | az motor torque | el motor torque | back-drives |
|---|---|---|---|---|
| 0.05 (greased, running) | 0.55 | 0.30 N·m | 0.06 N·m | no, the worm shaft seals hold it |
| 0.10 | 0.38 | 0.42 N·m | 0.07 N·m | no, the worm locks |
| 0.15 (from rest) | 0.29 | 0.55 N·m | 0.08 N·m | no, the worm locks |

The motor holds 0.45 N·m, and nothing turns the motors back at any of these. Of the az motor's
0.42 N·m at friction 0.1, the worm mesh takes 0.39, the worm shaft bearings 0.03 and the
spindle bearings 0.007. Driving az at 120 km/h with the 8.9 N·m reading has 6%
margin at friction 0.1 and stalls from rest; with the 6.3 N·m hand figure it needs 0.40 N·m
from rest. Park above about 80 km/h.

## Open

The gusty-side 16.6 N·m on the az wheel is more than the 7.4 N·m KHK lists for CG1-60R1
at 100 rpm, which is a wear rating. Check the static bending rating before trusting the
gears in a storm.
