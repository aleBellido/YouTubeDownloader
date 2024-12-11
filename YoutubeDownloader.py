import os
from pytubefix import YouTube
from tqdm import tqdm

if os.name == 'nt': #windows
    download_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
else: #linux/mac
    download_folder = os.path.join(os.environ['HOME'], 'Downloads')

url = input("Enter the URL -> ")

video = YouTube(url)

try:
    stream = video.streams.get_highest_resolution()

    print(f"Video '{video.title}' is downloading...")

    stream.download(download_folder)

    print(f"Video downloaded in {download_folder}")

except Exception as e:
    print(f"Error: {e}")
