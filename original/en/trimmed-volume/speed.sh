rm ../trimmed-volume-speed/*.mp3
for f in *.mp3; do
  ffmpeg -i "$f" -filter:a "atempo=1.1" "../trimmed-volume-speed/$f"
done