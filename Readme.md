# Steam Deck Repo Manager

A GUI interface to install boot videos on Steam Deck using [Steam Deck Repo](https://steamdeckrepo.com/) and GTK3. Thanks [Waylaidwanderer](https://www.reddit.com/user/waylaidwanderer) who created Steam Deck Repo !

![](https://raw.githubusercontent.com/CapitaineJSparrow/steam-repo-manager/main/screenshot.png)

## Installation

<a href='https://flathub.org/apps/details/com.steamdeckrepo.manager'><img width='200' alt='Download on Flathub' src='https://flathub.org/assets/badges/flathub-badge-en.png'/></a>

Steam Deck Repo Manager should be available in your distro Store, other wise run 

```
flatpak install --user flathub com.steamdeckrepo.manager
```

### Contribute

#### Requirements

* `build-essential gobject-introspection libcairo2-dev libjpeg-dev libgif-dev libgirepository1.0-dev` 
* python3.10+

```shell
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

#### Contributing on Windows

Download [MSYS2](https://www.msys2.org/), then open **mingw64** (not msys2)

```bash
pacman -Suy
pacman -S mingw-w64-x86_64-gtk3 mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject mingw-w64-x86_64-gst-python git
gtk3-demo #to check GTK is working
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py # Install pip manually since mingw packages are causing issues
python get-pip.py
python -m pip install -U --force-reinstall pip
rm get-pip.py
pip install -r requirements_windows.txt # Do not use a venv it's also causing issues ..
```

[Link to FlatHub repository](https://github.com/flathub/com.steamdeckrepo.manager)

![](https://raw.githubusercontent.com/CapitaineJSparrow/steam-repo-manager/main/testing.jpg)
