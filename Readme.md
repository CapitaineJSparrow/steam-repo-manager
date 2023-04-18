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

* A Linux OS
* `build-essential gobject-introspection libcairo2-dev libjpeg-dev libgif-dev libgirepository1.0-dev` 
* python3.10+

```shell
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

[Link to FlatHub repository](https://github.com/flathub/com.steamdeckrepo.manager)

![](https://raw.githubusercontent.com/CapitaineJSparrow/steam-repo-manager/main/testing.jpg)