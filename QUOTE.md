# Parts for quoting

`./export.sh` writes a STEP and a four-view SVG drawing for every made part into
`out/step/`, and the whole assembly to `out/rotator.step`. Tapped holes are modelled at
tap drill size; the thread is in the table.

## Plate parts (laser or waterjet cut, then drilled and tapped)

6082-T6 or 5083 aluminium, clear anodise or bare.

| part | qty | plate | holes |
|---|---|---|---|
| `bearing_plate` | 1 | 5 mm, 98 x 68 R6 | 4x Ø9 countersunk for M8; 2x M6; Ø20 |

## Machined

| part | qty | notes |
|---|---|---|
| `drive_block` | 2 | 6082-T6, 43 x 52 x 86 block; 2x Ø22 H7 x 7 (608), Ø14 thru, Ø22.4 motor pilot, 4x Ø3.4 on 31 square, 4x Ø4.5 in spine, 2x Ø3.4 beside the bearing seats (gear cover) |
| `worm_shaft` | 2 | steel (EN8 or silver steel) from Ø12 bar, 85 long: Ø11 x 13 shoulder, then Ø8 k6 for the 608s and worm, M8x1 x 8 thread at the far end; Ø5 D-bore, 4.52 across the flat, 18 deep in the shoulder end with a Ø5.1 x 3 round mouth, a sliding fit on the motor's D-cut shaft; a flat under the worm's M4 set screw, 20 to 26 from the thread end |
| `worm_spacer` | 6 | steel tube Ø12 x Ø8.1, faced square: 2 at 15, 2 at 3, 2 at 2 long |
| `mast_clamp` | 1 | 6082-T6, 200 x 136 x 10 flange on a Ø68 x 70 socket (weldment or machined from plate plus bar); Ø48.7 x 62 bore; 2.6 x 1.5 O-ring cord groove 4 mm in from the flange edge; blind 8 deep: 2x M6, 4x M8, 4x M4, 6x M3; 3x M8 radial |
| `flange_collar` | 1 | steel, Ø44 x 8 flange on a Ø24 x 12 hub; Ø15 H7 bore with 5 JS9 keyway; 4x Ø4.5 on 34 PCD; M5 set screw in the hub |
| `az_spindle` | 1 | Ø15 silver steel, 107 long; keyseat 5 P9 x 3 x 20 at 23 from the bottom end; keyseat 5 P9 x 3 x 18 open at the top end |
| `cross_clamp` | 1 | 6082-T6, 60 x 60 x 24 block, R4 corners; Ø25.2 saddle 6.6 deep along one side, Ø20.2 saddle 5 deep across the other; 8x Ø6.6 through |
| `yagi_boom` | 1 | 20 x 1.5 aluminium tube, 932 long; 14x Ø4.2 cross holes in two planes at 90°, see the drawing |
| `el_shaft` | 1 | Ø15 silver steel, 194.7 long; keyseat 5 P9 x 3 x 20 at 91.6 from one end; Ø5.2 cross holes at 17.35 and 177.35 |

## Printed

PETG, 4 perimeters, 30% infill. `az_gearcover_*` and `el_gearcover_*` STLs in `out/step/`,
already turned to print. Melt in five M3 heat-set inserts per low half (lid bosses) and two
in its trough ends.

| part | qty |
|---|---|
| `az_gearcover_low`, `az_gearcover_high` | 1 each |
| `el_gearcover_low`, `el_gearcover_high` | 1 each |

## Drilled enclosures

Two Hammond 1550Z220 die-cast boxes (IP66, gasket and lid screws included). Have both
KHK wheels reworked with an M4 set screw over the key as well as the 15 mm bore. The
`*_1550Z220` STEP files show where to drill:

- az box: floor 2x Ø6.5, 4x Ø8.5, 4x Ø4.5, 6x Ø3.4 (all into the mast clamp); M12x1.5 side wall (vent); 2x Ø16.2 end wall (glands)
- az lid: Ø20 (spindle)
- el box: Ø20 + 2x Ø6.5 floor (bearing unit), 4x Ø4.5 floor (el drive block); end wall Ø16 (spindle) and 4x Ø4.5 countersunk on 34 PCD (collar), with a Ø46 spot face inside, milled square to the floor to take out the wall's draft; Ø16.2 (gland) and M12x1.5 (vent) side wall
- el lid: Ø20 + 2x Ø6.5 (bearing unit)

## Bought

See `BOM.md` for every bought part with links and prices.
