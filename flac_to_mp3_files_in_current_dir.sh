for i in *.flac; do ffmpeg -i $i $"${i%.*}.mp3"; done
