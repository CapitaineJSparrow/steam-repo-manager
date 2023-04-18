import glob
import os
import requests

from pathlib import Path
from utils.slugify import slugify

movies_path = os.path.join(Path.home(), '.steam', 'root', 'config', 'uioverrides', 'movies')
library_path = os.path.join(Path.home(), '.local', 'share', 'Steam', 'steamui', 'library.js')
CURRENT_VERSION = "1.0.9"


def get_remote_version():
    response = requests.get(
        "https://raw.githubusercontent.com/CapitaineJSparrow/steam-repo-manager/main/flatpak/version.txt")
    return response.text.rstrip()


def list_installed_videos():
    files = [slugify(f.name) for f in Path(movies_path).iterdir() if f.is_file()]
    return files


def clear_installed_videos(_=None):
    # Ensure directory exists
    Path(movies_path).mkdir(parents=True, exist_ok=True)

    # Empty directory
    files = [f for f in Path(movies_path).iterdir() if f.is_file()]
    for f in files:
        f.unlink()
        print(f"{f} removed")


def download_video(_, url, title: str):
    print(f"Downloading {url}")
    response = requests.get(url)
    trucatedTitle = title[:75] if len(title) > 75 else title # Truncate title if > 75 chars
    Path(movies_path).mkdir(parents=True, exist_ok=True)
    open(os.path.join(Path(movies_path), slugify(trucatedTitle) + ".webm"), "wb").write(response.content)


def open_external(_, url: str = ''):
    os.system(f"xdg-open {url}")
