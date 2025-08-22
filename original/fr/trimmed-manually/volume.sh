for f in *.mp3; do
  ffmpeg -i "$f" -filter:a "volume=7dB" "../trimmed-volume/$f"
done