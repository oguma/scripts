out="${1%.*}.mp3"
ffmpeg-normalize -o $out -c:a libmp3lame -ar 44100 $1 &> /dev/null
