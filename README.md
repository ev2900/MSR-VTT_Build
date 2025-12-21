# MSR-VTT download and trim the videos from YouTube 

MSR-VTT (Microsoft Research Video-to-Text) is a benchmark dataset for video–language understanding.

The dataset consists of 10,000 short videos from YouTube. Due to copy write reasons, it is difficult to find a complete dataset with the video files, including audio. 

It is very easy to find the [metadata](https://github.com/ev2900/MSR-VTT_Build/blob/main/video_metadata.json) for each video.

I built this set of scripts so you can download the videos from YouTube and trim them to the specifications of the MSR-VTT benchmark.

## Install dependencies

The Python libraries can be installed via. 

```
pip install -r requirements.txt
```

Additionally, you have to install the command line tool [ffmpeg](https://www.ffmpeg.org/). 

The second script [1_trim_videos.py](https://github.com/ev2900/MSR-VTT_Build/blob/main/1_trim_videos.py) uses it to trim the full length videos downloaded in the first script [0_download_videos.py](https://github.com/ev2900/MSR-VTT_Build/blob/main/0_download_videos.py) this tool should be installed and added to your system path.

Reference the [ffmpeg download page](https://www.ffmpeg.org/download.html) for installation instructions.

## Download the videos

## Trim the videos
