for file in *.m4a; do
    ffmpeg -i "$file" -codec:a libmp3lame -qscale:a 2 "../${file%.m4a}.mp3"
done
