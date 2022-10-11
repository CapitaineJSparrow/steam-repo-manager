# Steam Deck Repo Manager

A GUI interface to install boot videos on Steam Deck using [Steam Deck Repo](https://steamdeckrepo.com/) using GTK3. Thanks [Waylaidwanderer](https://www.reddit.com/user/waylaidwanderer) who created Steam Deck Repo !

### Contribute

```bash
python3 -m venv ./venv
pip3 install -r requirements.txt
py3 main.py
```

### Flatpak build
```
# Create dependencies list for flatpak builder
python3 ./tools/flatpak-pip-generator.py --requirements=requirements.txt 
# Create a local repository
sudo flatpak-builder --repo=repo --force-clean out org.captainjsparrow.steamdeckrepo.yml
# Compile app into a single .flatpak
flatpak build-bundle ./repo steamdeckrepo.flatpak org.catainjsparrow.steamdeckrepo
# Install
sudo flatpak install steamdeckrepo.flatpak
```
