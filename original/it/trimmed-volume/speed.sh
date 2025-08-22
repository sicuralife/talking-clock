mkdir -p ../trimmed-volume-speed
for f in *.mp3; do
  ffmpeg -i "$f" -filter:a "atempo=1.1" "../trimmed-volume-speed/$f"
done