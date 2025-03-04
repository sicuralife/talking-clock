for file in *.mp3; do 
    ffmpeg -i "$file" -t $(ffmpeg -i "$file" 2>&1 | awk -F: '/Duration/ {print ($2*3600) + ($3*60) + $4 - 0.1}') ../../audio/it/"$file"
done