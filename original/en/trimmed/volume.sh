mkdir -p ../trimmed-volume
rm ../trimmed-volume/*.mp3
for f in *.mp3; do
  ffmpeg -i "$f" -filter:a "volume=5dB" "../trimmed-volume/$f"
done