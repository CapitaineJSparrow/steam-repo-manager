from random import randint

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gst', '1.0')

import asyncio
from ui import ui
import requests
import urllib3
import time

# Steam deck repo may have issue with SSL
urllib3.disable_warnings()


async def download_image(url, author, title, downloads, video, likes, duration):
    response = requests.get(url, verify=False)
    return {
        "content": response.content,
        "author": author,
        "title": title,
        "downloads": downloads,
        "video": video,
        "likes": likes,
        "duration": duration,
    }


async def get_videos(page: int, search: str = ''):
    start_time = time.time()
    search_query = f"&search={search}" if len(search) > 0 else ""
    url = f"https://steamdeckrepo.com/api/posts?page={page + 1}{search_query}"
    payload = {}

    response = requests.request("GET", url, data=payload)

    # Create an array of futures to gather them later
    images_list = list(map(
        lambda x: download_image(x["thumbnail"], x["user"]["steam_name"], x["title"], x["downloads"], x["video"], x["likes"], x["video_duration"]),
        response.json()["posts"]
    ))

    # Download images and metadata using parallelism
    videos = await asyncio.gather(*images_list)
    duration = time.time() - start_time
    print(f"Downloaded in {duration} seconds")
    return videos

PORTAL_BUS_NAME = "org.freedesktop.portal.Desktop"
PORTAL_OBJECT_PATH = "/org/freedesktop/portal/desktop"
PORTAL_SETTINGS_INTERFACE = "org.freedesktop.portal.Background"

async def main():
    ui.build_ui()

if __name__ == "__main__":
    asyncio.run(main())
