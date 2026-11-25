#!/bin/bash
mkdir -p final/parts

pairs=(
"Opening:01_opening"
"Hook:02_hook"
"AverageRate:03_average"
"SecantToTangent:04_secant_tangent"
"NumericalTable:05_table"
"Algebra:06_algebra"
"WorkedExample:07_example"
"Closing:08_closing"
)

i=1
for p in "${pairs[@]}"; do
  scene="${p%%:*}"
  aud="${p##*:}"
  v="media/videos/scenes/1080p60/$scene.mp4"
  a="audio/$aud.m4a"

  dv=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$v")
  da=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$a")

  T=$(awk -v a="$da" 'BEGIN{print a+1}')
  f=$(awk -v t="$T" -v v="$dv" 'BEGIN{f=t/v; if(f>2)f=2; if(f<1)f=1; print f}')
  vs=$(awk -v v="$dv" -v f="$f" 'BEGIN{print v*f}')
  pad=$(awk -v t="$T" -v s="$vs" 'BEGIN{p=t-s; if(p<0)p=0; print p}')

  echo "== $scene: slow x$f, freeze ${pad}s, total ${T}s"

  ffmpeg -y -loglevel error -i "$v" -i "$a" \
    -filter_complex "[0:v]setpts=${f}*PTS,tpad=stop_mode=clone:stop_duration=${pad},fps=60[v];[1:a]apad,aresample=48000[a]" \
    -map "[v]" -map "[a]" -t "$T" \
    -c:v libx264 -pix_fmt yuv420p -c:a aac -ar 48000 -b:a 192k \
    "final/parts/$(printf %02d $i)_$scene.mp4"
  i=$((i+1))
done
echo "Done."