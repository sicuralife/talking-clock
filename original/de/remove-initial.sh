for file in *.mp3; do
    ffmpeg -ss 1 -i "$file" -acodec copy "trimmed/${file%.mp3}.mp3"
done
