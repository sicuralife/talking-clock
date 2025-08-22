for f in *.mp3; do
  ffmpeg -i "$f" -filter:a "volume=10dB" "../trimmed-volume/$f"
done