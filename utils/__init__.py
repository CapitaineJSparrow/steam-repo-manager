import glob
import os
from pathlib import Path
import requests

movies_path = os.path.join(Path.home(), '.steam', 'root', 'config', 'uioverrides', 'movies')
library_path = os.path.join(Path.home(), '.local', 'share', 'Steam', 'steamui', 'library.js')
CURRENT_VERSION = "1.0.7"


def get_remote_version():
    response = requests.get("https://raw.githubusercontent.com/CapitaineJSparrow/steam-repo-manager/main/flatpak/version.txt")
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


def download_video(_, url: str):
    print(f"Downloading {url}")
    clear_installed_videos()
    response = requests.get(url)
    open(os.path.join(Path(movies_path), "deck_startup.webm"), "wb").write(response.content)
    override_default_length_library()


def open_external(_, url: str = ''):
    os.system(f"xdg-open {url}")
