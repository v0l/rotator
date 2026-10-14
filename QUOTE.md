# Parts for quoting

`./export.sh` writes a STEP and a four-view SVG drawing for every made part into
`out/step/`, and the whole assembly to `out/rotator.step`. Tapped holes are modelled at
tap drill size; the thread is in the table.

## Plate parts (laser or waterjet cut, then drilled and tapped)

6082-T6 or 5083 aluminium, clear anodise or bare. Two sets of drive plates, one per axis
(`parts/driveplates.gcad`); the edge holes are M3 tapped 8 deep into the plate edges.

| part | qty | plate | holes |
|---|---|---|---|
| `drive_side` | 4 | 10 mm, 29 x 44.5 | Ø22 H7 x 7 blind (608) on the inside face, Ø14 through; Ø3.4 (cover screw); 4x M3 x 8 in the edges (2 to the base, 2 to the top) |
| `drive_motor` | 2 | 6 mm, 43 x 44.5 | Ø22.4 (motor pilot); 4x Ø3.4 on 31 square; 4x M3 x 8 in the edges |
| `drive_base` | 2 | 6 mm, 30 x 87 | 4x M4 (sealing screws from the box); 6x Ø3.4 countersunk (plates) |
| `drive_top` | 2 | 6 mm, 29 x 87 | 6x Ø3.4 countersunk (plates); 4x M4 (az drive hangers) |
| `yoke` | 1 | 3 mm 5052-H32, laser cut from `out/step/yoke_flat.dxf` (50 wide, round ends), bent down 90° twice on the `BEND` lines at 3 mm inside radius to a 120 wide U, then two pressed darts in each bend (10 wide at the bend, 12 legs, at ±5 from the middle) | in the blank: Ø20.2 at each round end (hub boss) with 4x Ø5.4 on 31 PCD around it for M4 clinch nuts, pressed in from the outside; 4x Ø6.5 in the crossbar (tube U-bolts) |

## Machined

| part | qty | notes |
|---|---|---|
| `worm_shaft` | 2 | Ø8 silver steel, 83 long; Ø5 D-bore, 4.52 across the flat, 22 deep in one end with a Ø5.1 x 6 round mouth, a sliding fit on the motor's D-cut shaft; a flat under the worm's M4 set screw |
| `worm_spacer` | 4 | steel tube Ø12 x Ø8.1, faced square: 15 and 3 (az), 16 and 4 (el) |
| `flange_collar` | 1 | steel, Ø48 x 8 flange on a Ø28 x 12 hub; Ø17 H7 bore; Ø4 H7 cross hole through the hub (dowel); 4x Ø4.5 on 38 PCD; an O-ring groove or flat gasket on the flange face |
| `az_spindle` | 1 | turned and bored from 42CrMo4+QT (4140 pre-hard) bar: Ø17 h6 x 102.2, bore Ø13 through, ends chamfered and the bore deburred (cables pass); 2x Ø4 H7 cross holes at 33 and 88.2 from the bottom end (wheel and collar dowels, drill through with them fitted) |
| `el_shaft` | 1 | Ø12 silver steel, 131 long; keyseat 4 P9 x 2.5 x 18 at 54.5 from the floor end, ends radiused; keyways 4 P9 x 2.5 open at both ends, 8.5 long (arm hubs); M5 x 10 tapped in both ends |
| `el_hub` | 2 | steel, Ø40 x 6 flange on a Ø20 x 3 boss (the boss goes through the yoke arm); Ø12 H7 bore with 4 JS9 keyway through; 4x Ø4.5 on 31 PCD |
| `cross_clamp` | 1 | 6082-T6, 60 x 60 x 24 block, R4 corners; Ø25.2 saddle 6.6 deep along one side, Ø20.2 saddle 5 deep across the other; 8x Ø6.6 through |
| `yagi_boom` | 1 | 20 x 1.5 aluminium tube, 932 long; 14x Ø4.2 cross holes in two planes at 90°, see the drawing |
| `bracket_tube` | 1 | 25 x 2 aluminium tube, 390 long |
| gear rework | 4 | CG1-60R1: bore 17 H7, Ø4 H7 cross hole through the hub (dowel); SW1-R1 and SW0.8-R1: bore 8 H7; BG0.8-60R1: bore 12 H7, keyway 4 JS9, M4 set screw over the key |

## Printed

PETG, 4 perimeters, 30% infill. `az_gearcover_*` and `el_gearcover_*` STLs in `out/step/`,
already turned to print. Melt in four M3 heat-set inserts per low half (lid bosses) and two
in its trough ends.

| part | qty |
|---|---|
| `az_gearcover_low`, `az_gearcover_high` | 1 each |
| `el_gearcover_low`, `el_gearcover_high` | 1 each |
| `accessory_bracket` (optional, Pi and SDR), printed lying on its back wall; four M2.5 heat-set inserts in the bosses | 1 |
| `cable_guide`, printed standing on its Ø48 flange with tree supports under the run, so the tube's end clears the bed; the flange bolts to the box's bottom wall on the collar's four screws | 1 |

## Drilled enclosures

A Hammond 1550WH (az, 222 x 146 x 105) and a 1550Z117 (el, 160 x 100 x 81), both IP66 with
gasket and lid screws. The `*_1550*` STEP files show where to drill:

- az box, bottom wall: 2x Ø16.2 (glands), M12x1.5 (vent)
- az box, top wall: Ø21 (spindle), 2x Ø6.5 (KFL003 pair), 4x Ø4.5 (az drive hangers)
- az box, back wall: 4x Ø9 (mast U-bolts), 4x Ø3.4 (board standoffs), 2x Ø3.4 (battery holder)
- el box, floor: Ø16 + 2x Ø6.5 (KFL001), 4x Ø4.5 (el drive)
- el box, bottom end wall: 4x Ø4.5 on 38 PCD (collar and the cable guide flange), Ø14 (cables from the spindle)
- el box, top end wall: Ø16.2 (coax gland)
- el lid: Ø16 + 2x Ø6.5 (KFL001, mounted inside)

## Bought

See `BOM.md` for every bought part with links and prices.
