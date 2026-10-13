# Control board

One 88 x 80 mm, 4-layer board in the az box runs both axes from a single PoE cable. It is an
[agentee](https://github.com/v0l/agentee) project: `ctl.board.toml` (stackup, net classes,
isolation), five schematic sheets, `ctl.pcb.toml` (placed and routed), and the sims.

![Board](../docs/board.png)

## Blocks

| block | parts | notes |
|---|---|---|
| PoE in | J1 Bel V8BR-1AX1-GH vertical magjack, D1 D2 onsemi MDB10S silicon bridges, C1 10 nF, U1 Silvertel Ag5424 | 802.3at class 4, 24 V out. Data and spare pairs both rectified. The bridges are silicon, not Schottky: the idle bridge leaks across the PD signature during detection, and Comchip's curve for the CDBHM2100L-G puts that near 0.1 mA at 10 V once warm, enough to pull 25k under the 19k minimum. MDB10S leaks 10 uA max at 1000 V. C1 is the 10 nF the Ag5400 datasheet shows (figures 3 and 13); more would add to the module's own input capacitance in the detection signature. |
| AT detect | U2 LTV-357T, R1 24k, R2 47k | Ag5424 AT-DET across the barrier to PC13. R1 gives 1.7 mA at 42.5 V; the worst-case CTR there (50 % min at 5 mA, times 0.6 from figure 5) still sinks 0.5 mA, ten times what 47k needs. |
| 3V3 | U3 AP63201WU buck from VBUCK, 205k/62k sets 3.45 V, L1 6.8 uH | VBUCK is V24 through D4, or USB VBUS through D5, so the logic runs from USB on the bench. The rail is 3.45 V, not 3.3 V, because the encoders need 3.3 V at the end of a mux and a cable; every part on it is rated to 3.6 V. |
| Keep-alive | J10 CR123A lead, D10, U5 TPS61099 boost (487k/200k sets 3.44 V), U6 TPS2116 mux | VKEEP is 3V3 when it is up, otherwise the cell. MAIN_OK (U6 status) tells the MCU which. The whole group sits in the top right corner beside the encoder headers, so VKEEP reaches J4, J5 and the MCU without crossing the board. |
| MCU | U10 STM32H563RIT6 on VKEEP | No HSE: HSI, HSI48 with CRS for USB, LSE 32.768 kHz for the RTC. |
| Ethernet | U14 LAN8720A RMII, Y2 ECS-250-12-33B, R5 499R | The PHY makes the 50 MHz REF_CLK (nINTSEL strapped low by R29) and feeds PA1. Y2 is rated 200 uW and 12 pF, so it uses the LAN8720A's 100 uW crystal circuit (datasheet 5.6.2): R5 in series with XTAL2 and C60/C61 15 pF for 12 pF with 3 pF of pin capacitance. |
| Drivers | U12 U13 TMC2209 | UART only. STEP and DIR are tied low; the MCU moves the motors with VACTUAL. Shared MOT_EN, DIAG to PB1/PB2, 0.11 ohm sense. |
| Encoders | J4 J5 JST XH 5 pin, U16 U17 USBLC6-4SC6, 220 ohm series | Powered from VKEEP, so TIM2 (az) and TIM3 (el) keep counting through an outage. The 17HS15-1504-ME1K encoder wants 3.3 to 5.5 V (StepperOnline spec); VKEEP is 3.43 V. Only the + side of each differential output is used. |
| USB | J7 GCT USB4960 vertical USB-C, U15 USBLC6-2SC6 | Vertical so the plug goes in from above instead of into the az motor; the assembly has 35 mm of clear height over it. | DFU via BOOT0 (SW2). SWD on J6, a TC2030 pad with no part to fit. |

## MCU pins

| pin | function | pin | function |
|---|---|---|---|
| 1 | VBAT to VKEEP | 33 PB12 | RMII TXD0 |
| 2 PC13 | AT_DET | 36 PB15 | RMII TXD1 |
| 3, 4 | LSE | 37, 38, 39 PC6-8 | ENC_EL A, B, Z (TIM3) |
| 7 | NRST (SW1, J6) | 41 PA8 | ENC_AZ Z |
| 8 PC0 | VBAT_SENSE (cell / 2) | 44, 45 PA11, PA12 | USB DN, DP |
| 9 PC1 | MDC | 46, 49 | SWDIO, SWCLK |
| 10 PC2 | MAIN_OK | 50 PA15 | ENC_AZ A (TIM2 CH1) |
| 11 PC3 | PHY_RST | 51 PC10 | TMC_TX (through R46 1k) |
| 14 PA0 | status LED | 52 PC11 | TMC_UART |
| 15 PA1 | RMII REF_CLK | 55 PB3 | ENC_AZ B (TIM2 CH2) |
| 16 PA2 | MDIO | 60 | BOOT0 (R22 down, SW2 up) |
| 21 PA5 | RMII TX_EN | 30, 62 | VCAP, 2.2 uF each |
| 23 PA7 | RMII CRS_DV | 26 PB0 | MOT_EN |
| 24, 25 PC4, PC5 | RMII RXD0, RXD1 | 27, 28 PB1, PB2 | DIAG_AZ, DIAG_EL |

## Firmware notes

- Both TMC2209s share one half-duplex UART: U12 (az) is address 0, U13 (el) is address 1 (MS1
  low and high, MS2 low). In GCONF set `pdn_disable`, `mstep_reg_select` and clear
  `I_scale_analog`: VREF is tied to GND, so with the power-on default the run current is zero.
- Coil A of both motors is reversed at J8 and J9 to simplify routing. Set `shaft` in GCONF.
- Both motors at 1.4 A RMS take about 23 W from 24 V, which with the Ag5424 losses and the
  bridges is over the 25.5 W a class 4 device may draw. Drop IHOLD at standstill and do not
  run both axes at full current together.
- When MAIN_OK falls, put the RMII, MDIO, MDC and TMC UART pins in analog mode so VKEEP does
  not feed the unpowered PHY and drivers, drop the core clock, and keep TIM2 and TIM3 running.
  Write the positions to flash on stop. The outage current is not measured yet.
- Park az in high wind instead of driving it. With cold or dry grease (worm friction 0.15) the
  az motor needs 0.17 N·m at 60 km/h, 0.27 at 80, 0.33 at 90, 0.39 at 100 and 0.55 at 120 km/h
  (`sims/torque.gsim --set kmh=...`, wind torque 8.9 N·m at 120 km/h scaled with speed
  squared). The motor pulls about 0.36 N·m at 1.4 A RMS, so it drives to about 90 km/h with cold
  grease (100 km/h at friction 0.1, 0.31 N·m) and not at all at 120 km/h. 100 km/h puts 6.3 N·m
  through the wheel against KHK's 7.4 N·m rating for the CG1-60R1, 120 km/h 9.1 N·m. There is no
  anemometer, so judge the wind by the drive: when the az encoder lags the commanded position by
  more than a few degrees of motor turn, or StallGuard (SG_RESULT) falls near zero, halve
  VACTUAL and retry; after three stalls in a row stop az, report "parked: wind" and try again
  after 10 minutes. Parked, the worm locks while its friction is above tan(3.583°) = 0.063, and
  powered the motor holds against the 0.02 N·m the load can turn it back with; keep IHOLD at
  about 0.4 A (roughly 0.10 N·m) while parked for wind rather than dropping it to zero, since
  fresh grease can bring the friction near 0.05.
- VBAT_SENSE is the cell through a 1M / 1M divider.
- Set the RMII pins to GPIO speed high (OSPEEDR 10), not very high. `ctl-rmii` puts TXD1 (43 mm)
  at 10 % overshoot with very high edges (1.4 ns) and a 30 ohm driver, and under 2 % at high
  (1.9 ns); no RMII line needs termination at high.
- Y1 is an Epson FC-135 with CL 7 pF and ESR 70 kOhm max, which needs about 0.76 uA/V of
  oscillator gm (AN2867). Set LSEDRV to medium high (1.7 uA/V) or high; the low settings
  leave no margin. C21/C22 are 6.8 pF for 7 pF with about 3.5 pF of stray.

## Layout

- Stackup JLC041611-7628, ENIG. In1 is GND, In2 is 3V3, both outer layers poured GND.
- Primary (PoE) and secondary nets are separate domains with a 2 mm clearance, 2.5 mm
  creepage barrier. Under the Ag5424 the datasheet (V1.3, figure 12) wants no copper between
  15.3 and 42.1 mm from pin 1; a cutout on all four layers clears x 0 to 54.1, y 59.5 to 80.
- The barrier also holds through the board: In1 and In2 are cut out under every piece of
  primary copper (J1 centre taps, the bridges, R1, the opto input, POE_P and POE_N) with 2 mm
  to spare, so no secondary plane sits 0.2 mm under primary copper. GND reaches the chassis
  through H1 to H4, so the 802.3 1500 V isolation applies to it. POE_P and POE_N run 2.6 mm in
  from the left edge.
- With no inner planes under them, the bridges cool only through their own pours, so each
  bridge pin has a pour on both outer layers joined by four or five vias.
- No signal runs on In1 or In2.
- Only the two Ethernet pairs are impedance controlled. The field solver gives 96 ohm
  differential for the Eth class (0.24 mm, 0.2 mm gap, with mask) and 87 ohm for the USB pair.
  Both are short for their edges (100BASE-TX 3 ns, USB full speed 4 ns or slower), so the
  14 ps Ethernet skew and the 57 ps USB skew do not matter.
- The 3V3 buck keeps its loops on the top layer: C3 sits below U3 between VIN and GND, the
  inductor and output caps to its right, and the feedback divider on the back under FB.
- C2 is the Ag5424 output cap. The datasheet's operating conditions want 220 to 470 uF, so
  it is 330 uF and still passes at -20 %. It is as close to U1.8 as the module's courtyard
  allows, joined by a V24 pour.
- The U1 courtyard is the stepped keep-out of figure 14.
- The Ag5424 sheds heat through its output pins (datasheet section 4): pins 7, 8 and 10 join
  solid to a V24 pour and the GND pours on both outer layers, stitched with vias.
- Everything that must stay put is in `tools/place_fixed.txt`; the hand routes are in
  `tools/*_routes.txt`, the keep-alive group in `tools/keeper_place.txt`, the buck in
  `tools/buck_place.txt` and the pours, the module cutout and the primary plane cutout in
  `tools/zones.txt`. `tools/place.sh` rebuilds the placement from those files and wipes the
  routing.

## Sims

`agentee sim NAME` runs each one and writes `NAME.result.json`.

| sim | result |
|---|---|
| `ctl-dc-v24` | 0.96 A to the drivers and buck, 21 mV drop |
| `ctl-dc-motor` | 1.4 A per coil, 23 mV drop per side |
| `ctl-dc-3v3` | 240 mA from 3.45 V, worst 3.42 V at the MCU, 3.43 V at the encoders |
| `ctl-thermal` | 50 C inside the box, both motors at 1.4 A RMS: TMC2209 junctions 100 and 106 C, U1 output pins 126 C, D1 pads 123 C at 1.0 W (junction about 138 C of 150 C) |
| `ctl-thermal-1a` | same at 1.0 A RMS: drivers 80 and 83 C, U1 pins 102 C, D1 pads 88 C at 0.5 W |
| `ctl-eth` | FDTD of both 100BASE-TX pairs from the PHY pins, terminations and centre-tap decoupling in place: Sdd11 -48 dB (TX) and -51 dB (RX) at 100 MHz, -41 and -42 dB at 200 MHz; TX to RX differential crosstalk -44 dB at 100 MHz |
| `ctl-rmii` | FDTD of the seven RMII lines, a port at each end: insertion loss under 0.25 dB and crosstalk under -38 dB at 200 MHz, one-way delays 110 to 400 ps (TXD1 longest). `tools/rmii_step.py` turns it into the step at each receiver: with a 30 ohm driver TXD1 overshoots 10 % at 1.4 ns edges and 2 % at 1.9 ns, the PHY outputs under 6 % at 1 ns, REF_CLK none behind R35 |

The magjack pins are through-hole pads inside plane antipads, where agentee cannot place a port,
so `ctl-eth` has ports at the PHY only and sees the jack end as open; the magnetics are not
modelled. `tools/rmii_step.py` drives each RMII line from 30 and 50 ohm (the STM32 and LAN8720A
outputs are 0.4 V at 8 mA, so 50 ohm or less) into the receiver's pin capacitance (2 pF LAN8720A,
5 pF STM32) with a Gaussian edge; the LAN8720A gives no output edge time, so 1 ns stands in for
it.

The thermal sims send heat out through the four mounting holes at 5 C/W each, so the board
must sit on the aluminium M3 standoffs on the chassis plate. They also put all of the Ag5424
loss (2.3 W full load, 1.6 W typical, from its efficiency curve) into its output pins, which
makes the U1 pin temperature an upper bound. D1 takes the bridge loss: two diodes at about
0.85 V (MDB10S figure 1, typical at 0.6 A) and 0.6 A, the input current at 42.5 V and full load.

## Parts and fab

- `tools/bom.md` is the priced BOM, made by `python3 tools/bom.py` from Mouser (keys in
  `~/.config/agentee/distributors.toml`). Parts for one board come to about EUR 66 ex VAT.
- The STM32H563RIT6 is out of stock at Mouser, Farnell, LCSC and ST; Mouser expects 1941 on
  2026-12-11. Backorder it.
- J1 comes from Farnell (3588276).
- J7 has no vendor footprint in KiCad; `footprints/USB_C_Receptacle_GCT_USB4960_Vertical`
  is drawn from the GCT drawing (rev A, 2025-12-08). The stake slots are 1.2 x 0.6, long
  enough to drill at the 2:1 the fab needs, and the 0.72 x 0.52 peg slot is a round Ø0.75.
- No via needs plugging or filling. The only holes in pads are the footprint thermal vias in
  the exposed pads of U12 and U13 (16 each) and U14 (9), all 0.2 mm, open on top and tented
  from the bottom. Both datasheets ask for them: TMC2209 section 21.1 for heat (the drivers
  reach 106 C in `ctl-thermal`), and the LAN8720A pin table because the pad is its only VSS.
  The bottom tent traps air so the barrels take little of the paste. Order with tented vias
  and no via-in-pad process, and answer a fab query about these holes the same way.
- `agentee fab ctl -o fab` writes Gerbers, drill, placement and the JLCPCB BOM into `fab/`.
- `agentee parts ctl --spares --distributor mouser --order fab/order --no-alternatives` writes
  the Mouser cart (`fab/order/ctl-mouser.csv`, the top block is the order): about EUR 66 for one
  board with hand assembly spares, without U10 and J1. U1 has `spares = "0"`. The 0603 caps on the
  motor sheet are KEMET cut tape (`...TU`), since the Murata GCM and plain KEMET 4.7u sell in
  reels of 40000 and 4000 at Mouser.
- The CR123A holder is a Takachi CR123A-R with 140 mm leads; crimp a JST PHR-2 housing on.

## Vendor files

Not in the repo; download them to see the 3D models:

| file | from |
|---|---|
| `models/Ag5400_simplified.step` | Silvertel Ag5400 product page, CAD zip |
| `models/V8BR-1AX1-GH.stp` | Bel, V8BR-1AX1-GH product page (PARTserver) |

`tools/board_gcad.py` exports the board STEP with `agentee export`, takes the bounding box of
every part taller than 2.5 mm, and writes `../parts/ctl_board.gcad` for the assembly.
