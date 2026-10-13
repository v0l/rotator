#!/bin/sh
set -e
cd "$(dirname "$0")"
gcad=${GCAD:-gcad}
hammond=0
[ -f parts/vendor/1550Z220.stp ] && hammond=1
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
part bearing_plate parts/top_plate.gcad
part flange_collar parts/std/flangecollar.gcad "F=44 hub=24 pcd=34 screw=4.5"
part el_floor_plate parts/el_plates.gcad body=floor
part el_lid_plate parts/el_plates.gcad body=lid
part drive_block parts/driveblock.gcad
part worm_shaft parts/wormshaft.gcad
part mast_clamp parts/mastclamp.gcad body=main
part az_spindle parts/shaft.gcad "L=107 kz=23 kl=20 k2l=18"
part el_shaft parts/shaft.gcad "L=194.7 kz=86.6 kl=20 xh=1"
part cross_clamp parts/crossclamp.gcad
part yagi_boom parts/yagi435.gcad
part az_box_1550Z220 parts/std/hammond_1550z220_box.gcad "az=1 vendor=$hammond"
part az_lid_1550Z220 parts/std/hammond_1550z220_lid.gcad "az=1 vendor=$hammond"
part el_box_1550Z220 parts/std/hammond_1550z220_box.gcad "el=1 xe=26.75 vendor=$hammond"
part el_lid_1550Z220 parts/std/hammond_1550z220_lid.gcad "el=1 xe=26.75 vendor=$hammond"
print az_gearcover_low parts/gearcover.gcad "az=1 body=low" -90
print az_gearcover_high parts/gearcover.gcad "az=1 body=high" 90
print el_gearcover_low parts/gearcover.gcad "az=0 body=low" -90
print el_gearcover_high parts/gearcover.gcad "az=0 body=high" 90
"$gcad" export rotator.gasm out/rotator.step --set hammond=$hammond
