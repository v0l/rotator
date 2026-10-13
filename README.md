# Az/el antenna rotator

Weatherproof az/el rotator for small satellite yagis on a 25 mm crossboom, modelled in
[gcad](https://github.com/v0l/gcad). Housings are Hammond die-cast boxes; the made parts
are cut plates and a few turned and milled pieces, see `QUOTE.md`.

![Rotator](docs/rotator.png)

![Inside, box lids hidden](docs/inside.png)

![Turned to az 60°, el 30°](docs/posed.png)

```sh
gcad rotator.gasm                         # viewer, joints `az` and `el`
gcad check rotator.gasm                   # build, interference and joint sweeps
gcad render rotator.gasm out.png --set cover=0   # without the two box lids
gcad bom rotator.gasm
gcad export rotator.gasm rotator.step
```

## Layout

- Two Hammond 1550Z220 die-cast IP66 boxes: the az box on the mast, the el box standing
  on the az spindle 5 mm above the az lid. Every other made part is a cut plate, two short
  turned shafts, the flange collar, the mast clamp and the two drive blocks.
- The mast clamp's flange covers the underside of the az box and seals to it with one
  O-ring cord. Everything inside the az box screws through the floor into it: the lower
  bearing, the drive block, four M8 posts, the control board and the battery holder.
- Az: 15 mm spindle in two KFL002 flange units, one on the box floor and one under a
  bearing plate on the posts. The spindle leaves the lid through a V-ring and ends inside
  the el box in a keyed flange collar with a set screw, bolted to a spot face on the el
  box's end wall.
- El: 15 mm shaft in KFL002 units bolted outside the el box floor and lid, with backing
  plates inside. Crossboom tubes slide over the shaft ends on bronze bushes and are cross-bolted.
  The el axis is 226 mm above the az box floor, and the el head sits 14.75 mm off the az axis
  so the collar's bolts land in the box body, not the lid.
- Each axis: KHK CG1-60R1 wheel on a keyed shaft, KHK SW1-R1 worm on an 8 mm shaft in two
  608s in `driveblock.gcad`, jaw-coupled to a StepperOnline 17HS15-1504-ME1K closed-loop
  NEMA17 with a built-in 1000 PPR magnetic encoder. Turn counting and its battery backup
  live on the control board. The worm thread and the wheel teeth are helical at the 3.58°
  lead, so they mesh at every angle; `gcad check checks/worm_mesh.gasm` sweeps both pairs
  in half-degree steps. The helical wheel, the worm losses and the joint drag need gcad's `joint-drag` branch.
- Each worm and wheel runs in a PETG grease cover, `parts/gearcover.gcad` (`az=1` notches
  it round the bearing plate posts). It splits on the wheel's mid-plane: the low half takes
  two M3x14 through the drive block's plates and five M3 heat-set inserts, the high half
  screws onto it with five M3x10. The trough ends stop 0.5 mm short of the drive block
  plates, which close them. Fit the low half over the shaft before the wheel. Print the
  high half on its outer face; the low half stands on its worm trough and needs support
  under the wheel ring. `./export.sh` writes the four STLs turned that way.
- The boxes are `parts/std/hammond_1550z220_box.gcad` and `_lid.gcad`. Without
  Hammond's STEP they are drawn from its measurements. Download the STEP from
  https://www.hammfg.com/part/1550Z220, save it as `parts/vendor/1550Z220.stp`, and run
  with `--set hammond=1` to drill the real boxes; `./export.sh` uses it when present.

## 70 cm yagi

A crossed 7-element yagi for 435 MHz, cut from the DL6WU design in
[antenna toolbox](https://github.com/v0l/antenna-toolbox) (4 mm elements bonded through a
20 mm metal boom). Solved per plane: 11.9 dBi, F/B 30 dB, about 39 - j5 Ω at each driven
element. The two planes sit 25 mm apart along the boom in an X, 45° off the crossboom, and are
fed RHCP through a quarter-wave phasing harness. The model points it at the zenith (`el=90`).

| element | length | from the reflector |
|---|---|---|
| reflector | 346.4 | 0 |
| driven, tip to tip, split at the boom | 323.8 | 137.8 |
| D1 | 311.3 | 189.5 |
| D2 | 307.8 | 313.6 |
| D3 | 304.2 | 461.7 |
| D4 | 300.8 | 634.0 |
| D5 | 297.8 | 827.0 |

The second plane is the same set 25 mm further along. Parasitic lengths include DL6WU's
+10.8 mm boom correction. The boom (`parts/yagi435.gcad`) is 932 mm of 20 x 1.5 tube, with
40 mm past the reflector and the last director. It crosses the right-hand crossboom tube
300 mm out, at the yagi's balance point, on a milled cross clamp (`parts/crossclamp.gcad`)
held by four M6 U-bolts.

## Control board

`board/` is the controller in the az box: one PoE cable in, both motors and encoders out. An
STM32H563 with a LAN8720A PHY, two TMC2209 drivers on UART, a Silvertel Ag5424 PoE module, and
a CR123A cell that keeps the encoder counters alive through a power cut. It sits on four
aluminium M3 standoffs screwed into the mast clamp, which also carry its heat away. See
`board/DESIGN.md`.

![Control board](docs/board.png)

## Sealing

The boxes seal on their own gaskets. Shafts leave through V-rings against the bearing
units or the lid, cables through IP68 M16 glands, and each box has an M12 breather vent.
The mast clamp seals the floor holes with a face O-ring.

## Strength

`sims/` holds gcad FEA of the KFL002 housing, the spindle, the el shaft and the el box on
its collar under a 120 km/h gusty-side wind, and the bearing loads against the KFL002
ratings; see `sims/README.md`. The worst bearing sees 768 N against a 2.9 kN static rating,
and the shafts stay under 90 MPa away from the singular spots. The worm wheels are the open
question.

## Ratings

60:1 through a worm of 3.583° lead. The 17HS15-1504-ME1K pulls 0.42 to 0.43 N·m up to 210 rpm
at 1.69 A and 24 V (StepperOnline's pull-out curve), so about 0.36 N·m at the TMC2209's 1.4 A
RMS. At mesh friction 0.1 the worm is 38% efficient and locks, so the load cannot turn the motor.
`sims/torque.gsim` checks the motor torque against the wind at 90 km/h with cold grease
(friction 0.15): 0.33 N·m at 1 rpm, with the mesh at 39 MPa Lewis bending in the FC200 wheel
and 1.3 W of friction heat. Wind torque is taken as 8.9 N·m at 120 km/h (CFD) scaled with
speed squared, and every joint carries its bearing and seal drag.
KHK lists CG1-60R1 (cast iron) at 7.4 N·m at 100 rpm worm speed.
Az drives up to about 90 km/h of wind with cold grease (100 km/h with fresh) and parks above
that; the rule is in the firmware notes of `board/DESIGN.md`.
