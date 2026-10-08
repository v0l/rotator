#!/bin/sh
set -e
cd "$(dirname "$0")"
gcad=${GCAD:-gcad}
out=out/step
mkdir -p "$out"
part() {
  name=$1 file=$2 body=$3
  wrap="$out/.$name.gasm"
  if [ -n "$body" ]; then echo "part $name ../../$file body=$body" > "$wrap"; else echo "part $name ../../$file" > "$wrap"; fi
  "$gcad" export "$wrap" "$out/$name.step"
  "$gcad" export "$wrap" "$out/$name.svg"
  rm "$wrap"
}
part base_box parts/base.gcad main
part base_lid parts/base.gcad lid
part turret parts/turret.gcad
part column_left parts/column.gcad left
part column_right parts/column.gcad right
part drive_block parts/driveblock.gcad
part mast_clamp parts/mastclamp.gcad main
part el_shaft parts/elshaft.gcad
"$gcad" export rotator.gasm out/rotator.step
