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

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 ytpy.py -vi/-au \"<YouTube_URL>\"")
        sys.exit(1)

    flag = sys.argv[1]
    video_url = sys.argv[2]

    if flag == "-vi":
        download_media(video_url, "video")
    elif flag == "-au":
        download_media(video_url, "audio")
    else:
        print("Invalid flag! Use -vi for video or -au for audio.")
        sys.exit(1)