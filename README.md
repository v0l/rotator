# Az/el antenna rotator

Weatherproof az/el rotator for small satellite yagis on a U yoke, modelled in
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

`rotator.gasm` holds the az box and what is fixed to it (board, battery, glands, vent, mast
U-bolts) and brings in the sub-assemblies, joined by the `az` and `el` joints:

| file | in `rotator.gasm` as | what |
|---|---|---|
| `azstage.gasm` | `base` | both az KFL003s, the hollow spindle, wheel and dowels, flange collar, and the az worm drive as `base.drive` |
| `head.gasm` | `head` | el box and lid, el KFL001s, el shaft, wheel, U yoke, bracket tube, yagi, and the el worm drive as `head.drive` |
| `drive.gasm` | `base.drive` | az worm drive in its own frame (worm axis on z): cut plates, KHK SW1-R1 worm, 608s, worm shaft, spacers, NEMA17, grease cover |
| `drive_el.gasm` | `head.drive` | the same frame with the module 0.8 SW0.8-R1 worm and a cover for the BG0.8 wheel |

Screws that join a sub-assembly to something outside it live where both parts are. Each
sub-assembly opens, checks and simulates on its own: `gcad drive.gasm`, and
`sims/azdrive.gsim` loads `azstage.gasm`.

## Layout

- Az: a Hammond 1550WH (222 x 146 x 105, IP66) stands on its end beside the mast, held by two
  M8 U-bolts on V-saddles through its back wall. Its lid faces the front, so the control board
  and both az parts come out without touching the head.
- The az spindle is a short 17 x 2 steel tube, 102 long, on two KFL003s that sandwich the
  box's top wall on the same two M6 bolts, one outside and one inside, 25.5 mm apart. The
  wheel sits just under the inside one and the flange collar just above the outside one, both
  held by Ø4 cross dowels, so the torque path is short and the tube has no other holes. The
  tube is open at both ends: the el motor and encoder wires and the SDR coax drop straight out
  of its bottom end below the wheel cover, run up its 13 mm bore (an SMA plug and JST
  connectors pass), and come out inside the el box through a Ø14 hole in its floor, so they
  only twist over the ±270° travel. The collar flange seals against the el box and overhangs
  the outside KFL003 as a rain shield.
- El: a Hammond 1550Z117 (160 x 100 x 81) on the collar. A 12 mm el shaft crosses it on two
  KFL001s, the floor one outside, the lid one inside the lid. A U yoke laser cut from 3 mm 5052 and
  bent, with two pressed darts in each bend, is keyed straight onto both shaft ends and held by an M5 end screw and washer; the right arm
  clamps against a shaft collar outside the lid's V-ring. The head is 134 mm wide along the
  el axis. A 25 mm tube clamped to the yoke's crossbar carries the yagi 300 mm out, clear of
  the el box at every angle.
- Az drive: KHK CG1-60R1 wheel and SW1-R1 worm, 60:1. El drive: KHK BG0.8-60R1 bronze wheel and
  SW0.8-R1 worm, 60:1, 31 mm centres, small enough for the 1550Z117. Both run in the same
  cut-plate frame (`parts/driveplates.gcad`): a base plate, two 10 mm side plates with blind
  608 seats on their inside faces, a motor plate and a top plate, joined by countersunk M3
  screws into tapped plate edges. The worm and two spacers sit between the 608 inner rings,
  so the side plates capture the worm when they are screwed to the base plate; the worm's
  M4 set screw carries the torque. The plain 8 mm worm shaft has a D-bore at the motor end
  that slides over the StepperOnline 17HS15-1504-ME1K's D-cut shaft, so the motor passes
  torque only, with no coupling. The az drive hangs from the top wall on four 7.5 mm spacers,
  with M4 O-ring sealing screws from outside into its top plate; the el drive's base plate
  takes four M4 sealing screws through its box.
- Optional Raspberry Pi and SDR: a printed bracket (`parts/accessory_bracket.gcad`) hangs
  from the az drive's base plate on four M4 screws and drops a wall down into the space in
  front of the board. A Raspberry Pi 5 with a PoE HAT sits on four bosses with M2.5 heat-set inserts,
  facing the lid with its ports down, and an RTL-SDR Blog V4 is cable-tied flat to the wall
  beside it through two pairs of slots, USB plug down (a short USB lead to the Pi) and SMA up.
  The Pi's PoE cable uses the second bottom gland; the SDR's coax goes up the hollow spindle
  from just above the SMA. The Pi 5 model is laid out from the official STEP.
- Each worm and wheel runs in a PETG grease cover, `parts/gearcover.gcad`, split on the wheel's
  mid-plane, held to the side plates by two M3x14 into heat-set inserts.

## 70 cm yagi

A crossed 7-element yagi for 435 MHz, cut from the DL6WU design in
[antenna toolbox](https://github.com/v0l/antenna-toolbox) (4 mm elements bonded through a
20 mm metal boom). Solved per plane: 11.9 dBi, F/B 30 dB, about 39 - j5 Ω at each driven
element. The two planes sit 25 mm apart along the boom in an X, 45° off the bracket tube, and are
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
40 mm past the reflector and the last director. It crosses the bracket tube 300 mm out, at the
yagi's balance point, on a milled cross clamp (`parts/crossclamp.gcad`) held by four M6
U-bolts.

## Control board

`board/` is the controller in the az box: one PoE cable in, both motors and encoders out. An
STM32H563 with a LAN8720A PHY, two TMC2209 drivers on UART, a Silvertel Ag5424 PoE module, and
a CR123A cell that keeps the encoder counters alive through a power cut. It stands on four
10 mm aluminium M3 standoffs on the az box's back wall, facing the lid, held by O-ring sealing
screws from outside. See `board/DESIGN.md`.

![Control board](docs/board.png)

## Sealing

The boxes seal on their own gaskets. Every fixing through a box wall is an O-ring sealing
screw or has a sealing washer. The az spindle leaves the top wall through the two KFL003s,
whose insert seals and flanges close the hole, under the collar's rain shield; the el shaft leaves the floor through the outside KFL001's insert seal on an EPDM gasket,
and the lid through a V-ring. Cables crossing the az joint run inside the
hollow spindle; the coax leaves the el box through a gland in its top wall with a slack loop
to the yagi. A printed guide tube (`parts/cable_guide.gcad`) runs from under that gland down
the lid side of the el box, under the motor and into the floor hole, so a cable pushed in
through the top gland comes out of the spindle in the az box without opening either box; the
el motor and encoder wires drop into a slot in its floor run. The two PoE cables (board and Pi) use the glands in the az box's bottom wall,
beside the M12 breather vent.

## Strength

`sims/` holds gcad FEA under a 120 km/h wind; see `sims/README.md`. `azdrive` and `torque`
are current for this layout; the el shaft, el box and wind sims are from the old layout.

## Ratings

60:1 through a worm of 3.583° lead. The 17HS15-1504-ME1K pulls 0.42 to 0.43 N·m up to 210 rpm
at 1.69 A and 24 V (StepperOnline's pull-out curve), so about 0.36 N·m at the TMC2209's 1.4 A
RMS. At mesh friction 0.1 the worm is 38% efficient and locks, so the load cannot turn the motor.
`sims/torque.gsim` checks the motor torque against the wind at 90 km/h with cold grease
(friction 0.15): 0.33 N·m at 1 rpm, with the mesh at 39 MPa Lewis bending in the FC200 wheel
and 1.3 W of friction heat. Wind torque is taken as 8.9 N·m at 120 km/h (CFD) scaled with
speed squared, and every joint carries its bearing and seal drag.
KHK lists CG1-60R1 (cast iron) at 7.4 N·m at 100 rpm worm speed.
El: the same motor through the BG0.8-60R1 (3°17' lead) needs 0.15 N·m; the mesh carries 2.0 N·m
against KHK's 6.9 N·m at 100 rpm, 26 MPa Lewis bending in the bronze.
Az drives up to about 90 km/h of wind with cold grease (100 km/h with fresh) and parks above
that; the rule is in the firmware notes of `board/DESIGN.md`.
