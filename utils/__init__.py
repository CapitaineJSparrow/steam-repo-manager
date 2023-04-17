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


def override_default_length_library():
    f = open(library_path, "rb+")
    s = f.read()
    f.seek(0)
    s = s.replace(b'(s,1e4,[])', bytes(b"(s,4e4,[])"))
    f.write(s)
    f.close()


def clear_installed_videos(_=None):
    # Ensure directory exists
    Path(movies_path).mkdir(parents=True, exist_ok=True)

    # Empty directory
    files = glob.glob(f"{movies_path}/*")
    for f in files:
        print(f"{f} removed")
        os.remove(f)


def download_video(_, url, title: str):
    print(f"Downloading {url}")
    response = requests.get(url)
    trucatedTitle = (title[:75] + '..') if len(title) > 75 else title # Truncate title if > 75 chars
    Path(movies_path).mkdir(parents=True, exist_ok=True)
    open(os.path.join(Path(movies_path), slugify(trucatedTitle) + ".webm"), "wb").write(response.content)
    override_default_length_library()


def open_external(_, url: str = ''):
    os.system(f"xdg-open {url}")
