## Steam Deck Repo Manager

Steam Deck Repo Manager is a graphical user interface that allows you to install boot videos on your Steam Deck using [Steam Deck Repo](https://steamdeckrepo.com/) and GTK3. Thanks to [Waylaidwanderer](https://www.reddit.com/user/waylaidwanderer) for creating Steam Deck Repo!

![Screenshot of Steam Deck Repo Manager](https://raw.githubusercontent.com/CapitaineJSparrow/steam-repo-manager/main/screenshot.png)

### Installation

You can download Steam Deck Repo Manager from the [Flathub Store](https://flathub.org/apps/details/com.steamdeckrepo.manager), or install it via flatpak using the following command:

```bash
flatpak install --user flathub com.steamdeckrepo.manager
```

### Contributing

#### Requirements

- `build-essential gobject-introspection libcairo2-dev libjpeg-dev libgif-dev libgirepository1.0-dev`
- Python 3.10+

To get started with contributing, you can follow these steps:

```shell
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

#### Contributing on Windows

To contribute on Windows, you can follow these steps:

1. Download MSYS2.
2. Open mingw64 (not msys2).
3. Run the following commands:

```bash
pacman -Suy
pacman -S mingw-w64-x86_64-gtk3 mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject mingw-w64-x86_64-gst-python git
gtk3-demo # to check GTK is working
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py # Install pip manually since mingw packages are causing issues
python get-pip.py
python -m pip install -U --force-reinstall pip
rm get-pip.py
pip install -r requirements_windows.txt # Do not use a venv, it's also causing issues.
python main.py
```

If you want to build the app on Windows in a single .exe, you can install PyInstaller and run the following command:

```bash
pip install pyinstaller
pyinstaller -F --clean --add-data "./ui/icons/*;" main.py
```

![](https://raw.githubusercontent.com/CapitaineJSparrow/steam-repo-manager/main/testing.jpg)