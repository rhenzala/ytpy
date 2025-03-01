import yt_dlp
import os
import sys

def download_media(video_url, media_type):
    output_folder = os.path.expanduser("~/Downloads")
    if media_type == "video":
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(output_folder, "%(title)s.mp4")
        }
    elif media_type == "audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(output_folder, "%(title)s.mp3"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
            }]
        }
    else:
        print("Invalid flag! Use -vi for video or -au for audio.")
        sys.exit(1)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Download completed! Saved to {output_folder}")
    except Exception as e:
        print(f"An error occurred: {e}")