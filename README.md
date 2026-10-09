# Az/el antenna rotator

Weatherproof az/el rotator for small satellite yagis on a 25 mm crossboom, modelled in
[gcad](https://github.com/v0l/gcad). Housings are Hammond die-cast boxes; the made parts
are cut plates and a few turned and milled pieces, see `QUOTE.md`.

```sh
gcad rotator.gasm                         # viewer, joints `az` and `el`
gcad check rotator.gasm                   # build, interference and joint sweeps
gcad render rotator.gasm out.png --set cover=0   # without the two box lids
gcad bom rotator.gasm
gcad export rotator.gasm rotator.step
```

## Layout

- Two Hammond 1550Z220 die-cast IP66 boxes: the az box on the mast, the el box standing
  on the turret plate. Every other made part is a cut plate, two short turned shafts, the
  mast clamp and the two drive blocks.
- Az: 15 mm spindle in two KFL002 flange units, one on the chassis plate and one under a
  bearing plate on three standoffs. A flange collar on top carries the turret plate. The
  spindle leaves the lid through a V-ring.
- El: 15 mm shaft in KFL002 units bolted outside the el box floor and lid, with backing
  plates inside. Crossboom halves clamp in 15/25 rigid couplings.
- Each axis: KHK BG1-60R1 wheel on a keyed shaft, KHK SW1-R1 worm on an 8 mm shaft in two
  608s in `driveblock.gcad`, jaw-coupled to a dual-shaft NEMA17.
- Absolute magnetic encoder on each motor's rear shaft; turns are counted on a 1/2AA
  ER14250 cell in the base so position survives power loss.
- `parts/std/hammond_1550z220.gcad` is drawn from measurements of Hammond's STEP, which
  gcad cannot import yet (v0l/gcad#6).

## Sealing

The boxes seal on their own gaskets. Shafts leave through V-rings against the bearing
units or the lid, cables through IP68 M16 glands, and each box has an M12 breather vent.
The mast clamp seals the floor holes with a face O-ring.

## Ratings

60:1, 0.42 Nm motor, worm efficiency about 0.4: roughly 5 Nm usable at the output,
8-10 Nm at pull-out. KHK lists CG1-60R1 (cast iron) at 7.4 Nm at 100 rpm worm speed.
