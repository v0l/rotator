# Bill of materials, AliExpress version

Searched on AliExpress Ireland on 9 Oct 2026. Prices are in EUR with Irish VAT included,
and each is the listing's lowest option, so the size or quantity you need may cost
more. Delivery is usually free over €10 per seller.

## Bought on AliExpress

| qty | part | listing | from |
|---|---|---|---|
| 4 | KFL002 flange bearing, 15 mm (pack of 4) | [1005013055457662](https://www.aliexpress.com/item/1005013055457662.html) | €10.47 |
| 2 | Worm set, module 1, 60:1, brass wheel and steel worm | [1005007437546292](https://www.aliexpress.com/item/1005007437546292.html) | €11.02 each |
| 2 | STEPPERONLINE dual-shaft NEMA17, 40 mm, 45 Ncm | [32958088635](https://www.aliexpress.com/item/32958088635.html) | €12.63 each |
| 2 | Jaw coupling D20L25, 5 to 8 mm | [1005002758426926](https://www.aliexpress.com/item/1005002758426926.html) | €1.46 each |
| 4 | 608-2RS (pack of 10) | [1005013212915743](https://www.aliexpress.com/item/1005013212915743.html) | €6.04 |
| 2 | Shaft collar 8 mm | [1005004286453800](https://www.aliexpress.com/item/1005004286453800.html) | €1.49 |
| 1 | 303 stainless rod 15 mm, 300 mm (spindle and el shaft) | [4000186787300](https://www.aliexpress.com/item/4000186787300.html) | €6.02 |
| 1 | Stainless rod 8 mm, 200 mm (worm shafts) | [1005010787659558](https://www.aliexpress.com/item/1005010787659558.html) | €4.65 |
| 2 | AS5047P encoder adapter board | [1005005961434268](https://www.aliexpress.com/item/1005005961434268.html) | €9.32 each |
| 2 | Diametric magnet 6 x 2.5 for AS5047P | [1005012000796092](https://www.aliexpress.com/item/1005012000796092.html) | €12.60 |
| 3 | Cable gland M16, IP68 | [1005007639692634](https://www.aliexpress.com/item/1005007639692634.html) | €2.61 |
| 2 | Breather vent M12x1.5 | [1005005598068425](https://www.aliexpress.com/item/1005005598068425.html) | €9.23 |
| 3 | V-ring VA14 | [1005008984747262](https://www.aliexpress.com/item/1005008984747262.html) | €4.83 |
| 2 | Sintered bronze bush 15x21x20 | [1005010379695695](https://www.aliexpress.com/item/1005010379695695.html) | €4.60 each |
| 3 | M6 standoff, male-female, 304 stainless, 65 mm | [1005008723590685](https://www.aliexpress.com/item/1005008723590685.html) | €7.83 |
| 1 | Flange coupling 15 mm with keyway (turret) | [1005003216912431](https://www.aliexpress.com/item/1005003216912431.html) | €8.05 |
| 2 | Parallel key 5x5x20, 304 stainless | [1005010299052296](https://www.aliexpress.com/item/1005010299052296.html) | €6.86 |
| | A4 socket cap screws DIN 912, M3 to M6, one pack per size | [1005012860629584](https://www.aliexpress.com/item/1005012860629584.html) | about €25 |
| 3 | A4 countersunk screw M6x12, DIN 7991 | [1005011829285007](https://www.aliexpress.com/item/1005011829285007.html) | €7.23 |
| 1 | EPDM sheet 1 mm | [1005011772353226](https://www.aliexpress.com/item/1005011772353226.html) | €5.19 |

AliExpress subtotal from the listed prices: about **€196**.

## Still bought in Ireland

| qty | part | where | with VAT |
|---|---|---|---|
| 2 | Hammond 1550Z220 box | [Farnell 1823112](https://ie.farnell.com/hammond/1550z220/box-diecast-82x146x222mm/dp/1823112) | €92.20 |
| 1 | 25 mm aluminium tube, 1 m | [Goodwins](https://www.goodwins.ie/products/id-30577.html) | €10.95 |
| 1 | O-ring 86 x 2.5 EPDM | [Simply Bearings](https://www.simplybearings.ie/products/2-5x86-epdm) | €1.23 |

AliExpress has no die-cast box at 222 x 146 x 82, and the whole model is drawn around
the Hammond one. The IP67 cast boxes it does sell
([1005009587223023](https://www.aliexpress.com/item/1005009587223023.html), from €11.68)
come in several sizes; one would need at least 215 x 138 x 77 inside, and the box
model and drilling would have to be redone for it.

## Total

About **€300 with VAT**, against about €540 for the Irish, UK and EU suppliers in
`BOM.md`. Made parts are the same in both and still need quotes.

## Before ordering

- The AliExpress worm sets are not KHK parts. Check the listing's wheel and worm
  diameters: the drive blocks hold the worm 38 mm from the wheel centre, set by KHK's
  60.12 mm wheel and 16 mm worm. A different worm diameter needs `driveblock.gcad` and
  the box drilling moved.
- The 15 mm flange coupling replaces the turret's flanged collar; its flange diameter
  and bolt holes have to match `turret_plate.gcad`.
- Rod listed as 303 stainless is not ground to h6; check it fits the KFL002 bore and
  the wheel bore before cutting the keyways.
