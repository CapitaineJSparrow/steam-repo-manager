import asyncio

from ui import ui
import requests
import urllib3
import time

# Steam deck repo may have issue with SSL
urllib3.disable_warnings()


async def download_image(url, author, title, downloads, video):
    response = requests.get(url, verify=False)
    return {
        "content": response.content,
        "author": author,
        "title": title,
        "downloads": downloads,
        "video": video
    }


async def get_videos():
    start_time = time.time()
    url = "https://steamdeckrepo.com/api/posts"
    payload = {}

    response = requests.request("GET", url, data=payload)

    # Create an array of futures to gather them later
    images_list = list(map(
        lambda x: download_image(x["thumbnail"], x["user"]["steam_name"], x["title"], x["downloads"], x["video"]),
        response.json()["posts"]
    ))

    # Download images and metadata using parallelism
    videos = await asyncio.gather(*images_list)
    duration = time.time() - start_time
    print(f"Downloaded in {duration} seconds")
    return videos


async def main():
    ui.build_ui()

if __name__ == "__main__":
    asyncio.run(main())
