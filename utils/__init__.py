import glob
import os
from pathlib import Path
import requests

movies_path = os.path.join(Path.home(), '.steam', 'root', 'config', 'uioverrides', 'movies')
library_path = "/home/sparrow/Desktop/library.js"


def override_default_length_library():
    with open(library_path, 'r') as file:
        file_data = file.read()

    # Set 40 seconds, put a high limit does not cause any issue
    file_data = file_data.replace('(s,1e4,[])', '(s,4e4,[])')

    # Write the file out again
    with open(library_path, 'w') as file:
        file.write(file_data)


def clear_installed_videos(_=None):
    # Ensure directory exists
    Path(movies_path).mkdir(parents=True, exist_ok=True)

    # Empty directory
    files = glob.glob(f"{movies_path}/*")
    for f in files:
        print(f"{f} removed")
        os.remove(f)


def download_video(_, url: str):
    print(f"Downloading {url}")
    clear_installed_videos()
    response = requests.get(url)
    open(os.path.join(Path(movies_path), "deck_startup.webm"), "wb").write(response.content)
    override_default_length_library()


def open_external(_, url: str = ''):
    os.system(f"xdg-open {url}")
