rm ../mp3/*.mp3
for file in *.m4a; do
    ffmpeg -i "$file" -codec:a libmp3lame -qscale:a 2 "../mp3/${file%.m4a}.mp3"
done
