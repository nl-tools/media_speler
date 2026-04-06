import os
import json
import subprocess

# Paths
VIDEO_DIR = r"C:\Movies"
THUMB_DIR = "thumbnails"
THUMB_TIME = "00:00:30"

# Create thumbnails folder if it doesn't exist
os.makedirs(THUMB_DIR, exist_ok=True)

# Gather videos
files = [
    f"{VIDEO_DIR}/{f}"
    for f in os.listdir(VIDEO_DIR)
    if f.lower().endswith((".mp4", ".webm", ".mkv"))
]

# Generate thumbnails
for file_path in files:
    name = os.path.splitext(os.path.basename(file_path))[0]
    thumb_path = os.path.join(THUMB_DIR, f"{name}.jpg")

    # Skip if thumbnail already exists
    if not os.path.exists(thumb_path):
        subprocess.run([
            "ffmpeg",
            "-ss", THUMB_TIME,  # time to pick frame
            "-i", file_path,
            "-vframes", "1",
            "-q:v", "2",       # quality of JPEG
            thumb_path
        ])
        print(f"Thumbnail created: {thumb_path}")

# Save JSON list of videos
with open("videos.json", "w") as f:
    json.dump(files, f, indent=2)

print("videos.json updated!")