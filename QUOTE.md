# Parts for quoting

STEP and four-view SVG drawings for each machined part are written by `./export.sh` into
`out/step/`, with the whole assembly in `out/rotator.step`.

## Machined

Material 6082-T6 aluminium unless noted, clear anodise, break all edges 0.3.
Tapped holes are modelled at tap drill size.

| part | qty | stock | features |
|---|---|---|---|
| `base_box` | 1 | 140 x 212 x 80 block | pocket 68 deep, inner corners R12; Ø35 H7 x 11 bearing seat on floor boss, Ø28 through; 4x M6 x 10 underside; 10x M4 x 10 in wall tops; 2x M3 x 6 floor; 4x Ø4.5 thru, cbore Ø10 x 5 from underside; M12x1.5 thru floor (vent); 2x Ø16.2 thru +Y wall (glands) |
| `base_lid` | 1 | 140 x 212 x 30 plate | 6 mm spigot rim with O-ring groove 3.2 wide x 2 deep on its outside; Ø47 H7 x 19 bore (6005 + 25x47x7 seal), Ø32 thru; lip ring Ø120/Ø112 x 6; 10x Ø4.5 thru, cbore Ø8 x 4.5 |
| `turret` | 1 | Ø140 x 105 bar, turned | Ø15 h6 and Ø25 k6 journals; keyseat 5 P9 x 3 x 20 on Ø15; skirt Ø140/Ø126; 4x Ø5.5 thru, cbore Ø9.5 x 5.5 from underside |
| `column_left` | 1 | 50 x 136 x 207 block | pocket 29 deep from split face with screw lobes; O-ring face groove 3 wide x 1.9 deep on split face; boss Ø50 with Ø35 H7 x 18 bore (6202 + 15x35x7 seal), Ø20 thru; 8x Ø4.5 thru, cbore Ø10 x 5; 4x Ø4.5 thru (drive block); Ø16.2 thru (gland); M12x1.5 thru (vent); 2x M5 x 10 underside |
| `column_right` | 1 | 50 x 136 x 207 block | mirror pocket; boss Ø50 with Ø35 H7 x 18 bore, Ø20 thru; 8x M4 x 14 from split face; 2x M5 x 10 underside |
| `drive_block` | 2 | 43 x 51 x 102 block | 2x Ø22 H7 x 7 (608), Ø14 thru; Ø22.4 motor pilot; 4x Ø3.4 thru on 31 square; 4x M4 thru in spine |
| `mast_clamp` | 1 | Ø100 x 80 bar, turned | Ø48.7 x 62 bore for 48.3 mast; O-ring face groove Ø40-45.2 x 1.5 deep; 4x Ø6.6 thru, cbore Ø11 x 6.5; 3x M8 radial |
| `el_shaft` | 1 | Ø16 303 stainless | Ø15 h6 x 166; keyseat 5 P9 x 3 x 20 at 78 from one end; chamfer 0.5 both ends |

## Bought

| part | qty | note |
|---|---|---|
| KHK BG1-60R1 bronze worm wheel | 2 | J-series: bore 15 H7, keyway 5 JS9 |
| KHK SW1-R1 steel worm | 2 | rebore 8 H7 (stock bore 6) |
| NEMA17 17HS4401, dual shaft | 2 | rear shaft 5 x 7 for the encoder magnet |
| Magnetic absolute encoder board + 6x2.5 diametric magnet | 2 | MT6835 or AS5047P class |
| ER14250 1/2AA 3.6 V cell + holder | 1 | keeps the encoder turn counters alive |
| 5 to 8 mm jaw coupling D20 L25 | 2 | |
| Rigid clamp coupling 15 / 25 mm, Ø45 x 64 | 2 | crossboom clamps |
| Ground shaft 8 h6 x 85 | 2 | worm shafts |
| 608-2RS | 4 | |
| 6202-2RS | 3 | |
| 6005-2RS | 1 | |
| Shaft seal 15x35x7, 25x47x7 (DIN 3760) | 2, 1 | |
| Shaft collar 8 mm, 15 mm (DIN 705) | 2, 1 | |
| Key 5x5x20 (DIN 6885 A) | 2 | |
| Shim 15x21x1 (DIN 988), spacer 15x20x6 | 2, 1 | |
| O-ring cord 2.5 mm (lid, column), O-ring 40x2 (mast clamp) | | |
| M16 IP68 cable gland, M12x1.5 breather vent | 3, 2 | |
| ISO 4762 A4: M3x6 (2), M3x10 (8), M4x12 (18), M4x40 (8), M5x16 (4), M6x12 (4) | | bonded seal washers under the M4x40 and drive block screws |
| Aluminium tube 25 x 2 x 500 | 2 | crossboom |
