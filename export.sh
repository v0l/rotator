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
part chassis parts/chassis.gcad body=chassis
part bearing_plate parts/chassis.gcad body=top
part turret_plate parts/turret_plate.gcad
part el_floor_plate parts/el_plates.gcad body=floor
part el_lid_plate parts/el_plates.gcad body=lid
part drive_block parts/driveblock.gcad
part mast_clamp parts/mastclamp.gcad body=main
part az_spindle parts/shaft.gcad "L=98 kz=23 kl=20"
part el_shaft parts/shaft.gcad "L=194.7 kz=86.6 kl=20"
part az_box_1550Z220 parts/std/hammond_1550z220.gcad "az=1 body=box"
part az_lid_1550Z220 parts/std/hammond_1550z220.gcad "az=1 body=lid"
part el_box_1550Z220 parts/std/hammond_1550z220.gcad "el=1 xe=29.75 body=box"
part el_lid_1550Z220 parts/std/hammond_1550z220.gcad "el=1 xe=29.75 body=lid"
"$gcad" export rotator.gasm out/rotator.step
