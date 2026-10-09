# Parts for quoting

`./export.sh` writes a STEP and a four-view SVG drawing for every made part into
`out/step/`, and the whole assembly to `out/rotator.step`. Tapped holes are modelled at
tap drill size; the thread is in the table.

## Plate parts (laser or waterjet cut, then drilled and tapped)

6082-T6 or 5083 aluminium, clear anodise or bare.

| part | qty | plate | holes |
|---|---|---|---|
| `chassis` | 1 | 6 mm, 190 x 110 R5 | 4x Ø6.6; 5x M6 (2 bearing, 3 standoff); 4x M4; 2x M3 |
| `bearing_plate` | 1 | 5 mm, 98 x 68 R6 | 3x Ø6.5 countersunk Ø12.4 90°; 2x M6; Ø20 |
| `turret_plate` | 1 | 6 mm, 100 x 170 R10 | 4x M5; 4x Ø6.5 |
| `el_floor_plate` | 1 | 5 mm, 88 x 107 R5 | 2x Ø6.5; Ø20; 4x M4 |
| `el_lid_plate` | 1 | 5 mm, 60 x 80 R5 | 2x Ø6.5; Ø20 |

## Machined

| part | qty | notes |
|---|---|---|
| `drive_block` | 2 | 6082-T6, 43 x 52 x 104 block; 2x Ø22 H7 x 7 (608), Ø14 thru, Ø22.4 motor pilot, 4x Ø3.4 on 31 square, 4x Ø4.5 in spine |
| `mast_clamp` | 1 | 6082-T6, turned from Ø100 bar; Ø48.7 x 62 bore; O-ring face groove Ø86-91.2 x 1.5; 4x M6 x 9; 3x M8 radial |
| `az_spindle` | 1 | Ø15 h6 ground stainless rod, 98 long; keyseat 5 P9 x 3 x 20 at 23 from the bottom end |
| `el_shaft` | 1 | Ø15 h6 ground stainless rod, 194.7 long; keyseat 5 P9 x 3 x 20 at 86.6 from one end |

## Drilled enclosures

Two Hammond 1550Z220 die-cast boxes (IP66, gasket and lid screws included). The
`*_1550Z220` STEP files show where to drill:

- az box: 4x Ø6.5 floor (mast clamp), M12x1.5 floor (vent), 2x Ø16.2 end wall (glands)
- az lid: Ø20 (spindle)
- el box: Ø20 + 2x Ø6.5 floor (bearing unit), 4x Ø6.5 end wall (turret), Ø16.2 (gland) and M12x1.5 (vent) side wall
- el lid: Ø20 + 2x Ø6.5 (bearing unit)

## Bought

See `BOM.md` for every bought part with links and prices.
