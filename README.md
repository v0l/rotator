# Az/el antenna rotator

Weatherproof az/el rotator for small satellite yagis on a 25 mm crossboom, modelled in
[gcad](https://github.com/v0l/gcad). Housings are CNC aluminium; everything else is
catalogue parts.

```sh
gcad rotator.gasm                         # viewer, joints `az` and `el`
gcad check rotator.gasm                   # build, interference and joint sweeps
gcad render rotator.gasm out.png --set cover=0   # without the base box and lid
gcad bom rotator.gasm
gcad export rotator.gasm rotator.step
```

## Layout

- Az: solid spindle turned into the turret, 6202 below and 6005 + 25x47x7 lip seal in the lid.
  KHK BG1-60R1 wheel (rebored 15H7, keyway) driven by a KHK SW1-R1 worm.
- El: clamshell column split across the el axis, 6202-2RS + 15x35x7 lip seal in each half,
  15 mm keyed shaft, same worm set. Crossboom halves clamp in 15/25 rigid couplings.
- Each worm runs on an 8 mm shaft in two 608 bearings in `driveblock.gcad`, coupled to a
  dual-shaft NEMA17 (17HS4401) with a 5-8 jaw coupling.
- Absolute magnetic encoder on each motor's rear shaft; turns are counted on a 1/2AA
  ER14250 cell in the base so position survives power loss.

## Sealing

Lid: O-ring cord in a radial groove on the lid spigot. Column: cord in a face groove on
the left half. Mast clamp: face O-ring. Shafts: lip seals outboard of sealed bearings,
labyrinth skirt on the turret. Cables through IP68 M16 glands, M12 breather vent in each
enclosure. Use bonded seal washers under the column and drive block screws.

## Ratings

60:1, 0.42 Nm motor, worm efficiency about 0.4: roughly 5 Nm usable at the output,
8-10 Nm at pull-out. KHK lists CG1-60R1 (cast iron) at 7.4 Nm at 100 rpm worm speed.
