# Steam Deck Repo Manager

A GUI interface to install boot videos on Steam Deck using [Steam Deck Repo](https://steamdeckrepo.com/) and GTK3. Thanks [Waylaidwanderer](https://www.reddit.com/user/waylaidwanderer) who created Steam Deck Repo !

![](https://raw.githubusercontent.com/CapitaineJSparrow/steam-repo-manager/main/screenhot.png)

## Installation

<a href='https://flathub.org/apps/details/com.steamdeckrepo.manager'><img width='200' alt='Download on Flathub' src='https://flathub.org/assets/badges/flathub-badge-en.png'/></a>

Steam Deck Repo Manager should be availablle in your distro Store, other wise run 

```
flatpak install --user flathub com.steamdeckrepo.manager
```

### Contribute

```shell
python3 -m venv ./venv
pip3 install -r requirements.txt
py3 main.py
```

### Flatpak build
```shell
# Create dependencies list for flatpak builder
python3 ./tools/flatpak-pip-generator.py --requirements=requirements.txt 
# Create a local repository
sudo flatpak-builder --repo=repo --force-clean out com.steamdeckrepo.manager.yml
# Compile app into a single .flatpak
flatpak build-bundle ./repo steamdeckrepo.flatpak com.steamdeckrepo.manager
# Install
sudo flatpak install steamdeckrepo.flatpak
```
