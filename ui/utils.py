import os
from pathlib import Path
import requests
import glob


def open_external(_, url: str = ''):
    os.system(f"xdg-open {url}")


def download_video(_, url: str):
    dest_path = os.path.join(Path.home(), '.steam', 'root', 'config', 'uioverrides', 'movies')

    # Ensure directory exists
    Path(dest_path).mkdir(parents=True, exist_ok=True)

    # Empty directory
    files = glob.glob(f"{dest_path}/*")
    for f in files:
        os.remove(f)

    response = requests.get(url)
    open(os.path.join(Path(dest_path), "deck_startup.webm"), "wb").write(response.content)
