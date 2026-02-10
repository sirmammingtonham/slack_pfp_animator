import os
from slack_sdk import WebClient
from pathlib import Path
import datetime

# Load your token from an env var
SLACK_TOKEN = os.environ["SLACK_USER_TOKEN"]
client = WebClient(token=SLACK_TOKEN)

# Point this at a folder of pre-prepared square images
IMAGES_DIR = Path("./directors_cut")


def set_avatar():
    # Pick this minute’s image (cycles every minute)
    images = sorted(IMAGES_DIR.glob("*.png"))
    minute_count = int(datetime.datetime.now().timestamp() / 60)
    idx = minute_count % len(images)
    img_path = images[idx]

    with img_path.open("rb") as img:
        client.users_setPhoto(image=img)
    print(f"Set avatar to {img_path.name!r}")


if __name__ == "__main__":
    set_avatar()
