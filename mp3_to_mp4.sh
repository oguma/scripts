out="${1%.*}.mp4"
ffmpeg -f lavfi -i color=c=0x0a8c84:s=1280x720 -i $1 -shortest -fflags +shortest $out
