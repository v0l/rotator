#!/bin/sh
set -e
cd "$(dirname "$0")"
gcad=${GCAD:-gcad}
out=out/step
rm -rf "$out"
mkdir -p "$out"
part() {
  name=$1 file=$2 args=$3
  wrap="$out/.$name.gasm"
  echo "part $name ../../$file $args" > "$wrap"
  "$gcad" export "$wrap" "$out/$name.step"
  "$gcad" export "$wrap" "$out/$name.svg"
  rm "$wrap"
}
print() {
  name=$1 file=$2 args=$3 turn=$4
  wrap="$out/.$name.gasm"
  printf 'part %s ../../%s %s\nrotate %s %s axis=x\n' "$name" "$file" "$args" "$name" "$turn" > "$wrap"
  "$gcad" export "$wrap" "$out/$name.stl"
  rm "$wrap"
}
part drive_side parts/driveplates.gcad body=side_b
part drive_motor parts/driveplates.gcad body=motor
part drive_base parts/driveplates.gcad body=base
part drive_top parts/driveplates.gcad body=top
part yoke parts/yoke.gcad
part flange_collar parts/std/flangecollar.gcad "F=44 hub=24 pcd=34 screw=4.5"
part worm_shaft parts/wormshaft.gcad
part az_spindle parts/shaft.gcad "L=257 kz=23 kl=20 k2l=18"
part el_shaft parts/shaft.gcad "d=12 key=4 kd=2.5 L=119 kz=48.5 kl=18 k0l=6 k2l=5.5 tap=1"
part cross_clamp parts/crossclamp.gcad
part yagi_boom parts/yagi435.gcad
part bracket_tube parts/std/tube.gcad "D=25 t=2 L=390"
part az_box_1550WH parts/std/hammond_1550h.gcad body=main
part el_box_1550Z117 parts/std/hammond_1550z117.gcad body=main
part el_lid_1550Z117 parts/std/hammond_1550z117.gcad body=lid
print az_gearcover_low parts/gearcover.gcad "az=0 body=low" -90
print az_gearcover_high parts/gearcover.gcad "az=0 body=high" 90
print el_gearcover_low parts/gearcover.gcad "az=0 cx=31 R=27.4 rc=25.5 g=5 wr=8.5 wx2=10 bo=30.5 hub=27 shaft=14 body=low" -90
print el_gearcover_high parts/gearcover.gcad "az=0 cx=31 R=27.4 rc=25.5 g=5 wr=8.5 wx2=10 bo=30.5 hub=27 shaft=14 body=high" 90
"$gcad" export rotator.gasm out/rotator.step
