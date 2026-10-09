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

| part | qty | note | where |
|---|---|---|---|
| Hammond 1550Z220 | 2 | | Farnell 1823112, RS 228-7742, Mouser, TME |
| KFL002 flange bearing unit, 15 mm | 4 | 1 mm EPDM gasket under the two on the el box | bearing shops (Simply Bearings, Ashley Bearings), RS |
| KHK BG1-60R1 bronze worm wheel | 2 | J-series: bore 15 H7, keyway 5 JS9 | R.A. Rodriguez (rargears.com), KHK's UK and EU distributor |
| KHK SW1-R1 steel worm | 2 | rebore 8 H7 | R.A. Rodriguez |
| NEMA17 17HS4401, dual shaft | 2 | rear shaft 5 x 7 for the encoder magnet | StepperOnline (dual-shaft 17HS4401 variant) |
| Magnetic absolute encoder board + 6x2.5 diametric magnet | 2 | MT6835 or AS5047P class | Mouser or DigiKey (MT6835 or AS5047P eval boards), or own PCB |
| ER14250 1/2AA 3.6 V cell + holder | 1 | keeps the turn counters alive | Farnell, RS |
| 5 to 8 mm jaw coupling D20 L25 | 2 | | RS, Amazon, AliExpress |
| Rigid clamp coupling 15 / 25 mm, Ø45 x 64 | 2 | crossboom | Ruland via RS or Misumi, check the 25 x 15 bore pair |
| Flange shaft collar 15 mm, Ø50 flange, 4x Ø5.5 on 38 PCD | 1 | turret | Misumi, Ruland, Stafford |
| Ground shaft 8 h6 x 85 | 2 | worm shafts | Misumi (cut to length), linear-motion shops |
| 608-2RS | 4 | | any bearing shop |
| Shaft collar 8 mm | 2 | | RS, Accu, Misumi |
| V-ring VA-15 | 3 | | bearing and seal shops (SKF / Simrit VA-15) |
| Key 5x5x20 (DIN 6885 A) | 2 | | Accu, RS |
| Shim 15x21x1 (DIN 988) | 2 | | Accu, RS |
| Hex standoff M6 x 65, male-female | 3 | | RS, Accu |
| O-ring 86x2.5 | 1 | mast clamp | RS, any O-ring shop |
| M16 IP68 cable gland, M12x1.5 breather vent | 3, 2 | | Farnell, RS (Lapp Skintop, Amphenol LTW vents) |
| A4 screws: M3x6 (2), M3x10 (8), M4x10 (8), M5x12 (4), M6x10 (2), M6x12 (2), M6x12 countersunk (3), M6x16 (8), M6x20 (4), M6 nuts (8) | | sealing washers under the screws that pass through box walls | Accu |
| Aluminium tube 25 x 2 x 500 | 2 | crossboom | metal stockist |
