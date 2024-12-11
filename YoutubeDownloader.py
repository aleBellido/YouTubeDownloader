import os
from pytubefix import YouTube
from tqdm import tqdm

if os.name == 'nt':
    download_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
else:
    download_folder = os.path.join(os.environ['HOME'], 'Downloads')

url = input("Introduce la url -> ")

video = YouTube(url)

try:
    stream = video.streams.get_highest_resolution()

    print(f"El video '{video.title}' se está descargando...")

    stream.download(download_folder)

    print(f"Video instalado en {download_folder}")

except Exception as e:
    print(f"Error: {e}")
