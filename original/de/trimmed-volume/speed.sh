mkdir -p ../trimmed-volume-speed
for f in *.mp3; do
  ffmpeg -i "$f" -filter:a "atempo=1.2" "../trimmed-volume-speed/$f"
done