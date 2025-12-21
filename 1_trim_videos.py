import subprocess
from pathlib import Path
import json

# Check if output directory exists, if it does not create it
out_dir = Path('1_trim_videos')
out_dir.mkdir(exist_ok=True)

# Open MSR-VTT metadata
with open('video_metadata.json', 'r') as f:
    video_metadata = json.load(f)

# Get list of all files in the 0_full_videos folder
folder = Path("0_full_videos")
files = [f for f in folder.iterdir() if f.is_file()]

# Iterate over the files
for f in files:
    file_name = f.name.replace('.mp4', '')

    result = next(
        (item for item in video_metadata["videos"] if item["video_id"] == file_name),
        None
    )

    cmd = [
        "ffmpeg", "-y",
        "-ss", str(result['start time']),
        "-i", str(f'0_full_videos/{file_name}.mp4'),
        "-t", str(float(result['end time']) - float(result['start time'])),
        "-c", "copy",
        str(f'1_trim_videos/{file_name}.mp4')
    ]
    
    subprocess.run(cmd, check=True)
