from yt_dlp import YoutubeDL
import json
from pathlib import Path

# Function to dowload the YouTube video via. yt_dlp
def dowload_video(url, video_id):
    ydl_opts = {
        "format": 'best[ext=mp4][acodec!=none]/best[acodec!=none]/best',
        "outtmpl": f'0_full_videos/{video_id}.mp4',
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Check if output directory exists, if it does not create it
out_dir = Path('0_full_videos')
out_dir.mkdir(exist_ok=True)

# Open MSR-VTT metadata
with open('video_metadata.json', 'r') as f:
    video_metadata = json.load(f)

# Interate through the metadata and download the videos
number_of_videos_to_download = 10 # Upto 9999
videos_downloaded = 0

for video in video_metadata['videos']:
    if videos_downloaded >= number_of_videos_to_download:
        break
    else:
        try:
            dowload_video(video['url'], video['video_id'])
        except Exception as err:
            # write error to a error log file
            with open('error_log.txt', 'a') as e:
                e.write(f"{video['video_id']}, {err}\n")
            next
        
        videos_downloaded = videos_downloaded + 1
