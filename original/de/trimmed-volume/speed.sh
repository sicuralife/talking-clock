#!/bin/bash
rm ../trimmed-volume-speed/*.mp3 

# 1️⃣ Minutes files (1.mp3 → 59.mp3)
for f in [1-9].mp3 [1-5][0-9].mp3; do
  [ -e "$f" ] || continue  # skip if no match
  echo "Processing minute file: $f (1.25x)"
  ffmpeg -i "$f" -filter:a "atempo=1.25" "../trimmed-volume-speed/$f"
done

# 2️⃣ All other mp3 files
for f in *.mp3; do
  # Skip minute files
  if [[ "$f" =~ ^([1-9]|[1-5][0-9])\.mp3$ ]]; then
    continue
  fi
  echo "Processing other file: $f (1.2x)"
  ffmpeg -i "$f" -filter:a "atempo=1.2" "../trimmed-volume-speed/$f"
done
