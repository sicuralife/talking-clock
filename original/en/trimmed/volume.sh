mkdir -p ../trimmed-volume
for f in *.mp3; do
  ffmpeg -i "$f" -filter:a "volume=5dB" "../trimmed-volume/$f"
done