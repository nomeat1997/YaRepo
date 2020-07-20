import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
from colorthief import ColorThief
import urllib.request
import socket
import time
import secrets

input_client_id = "" #Enter your Client ID here
input_secret_id = "" #Enter your Client Secret here

def bar_sender(arr, total):
    udp_ip = "192.168.31.54"
    udp_port = 7777
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    s.connect((udp_ip, udp_port))
    barr = bytearray()
    for i in arr:
        barr.extend(i)
    print(f"Sent to esp {total} times.")
    s.send(barr)
    s.close()


def dl_album(url, file_path, file_name):
    full_path = file_name + ".jpg"
    urllib.request.urlretrieve(url, full_path)


# Get the username from terminal
username = sys.argv[1]
scope = "user-read-private user-read-playback-state user-modify-playback-state"

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(
        username,
        scope,
        client_id=input_client_id,
        client_secret=input_secret_id,
        redirect_uri="http://www.google.com/",
    )  # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(
        username,
        scope,
        client_id="f29581b0e9a349da809fc0485db1033e",
        client_secret="495de11ad1094857ba25d6c295a3ae23",
        redirect_uri="http://www.google.com/",
    )  # add scope

# Create our spotify object with permissions
spotifyObj = spotipy.Spotify(auth=token)


# User information
user = spotifyObj.current_user()
displayName = user["display_name"]
followers = user["followers"]["total"]
print()
print(f" >>> Welcome to Spotipy {username} !")
print(f" >>> You have {followers} followers.")

# Get current device
devices = spotifyObj.devices()
deviceID = devices["devices"][0]["id"]
deviceName = devices["devices"][0]["name"]

# Current track information
trackinfo = spotifyObj.current_user_playing_track()
# print(json.dumps(trackinfo, sort_keys=True, indent=4))
artist = trackinfo["item"]["album"]["artists"][0]["name"]
track = trackinfo["item"]["name"]
album = trackinfo["item"]["album"]["name"]
albumArt = trackinfo["item"]["album"]["images"][0]["url"]
albumArtSize = str(trackinfo["item"]["album"]["images"][0]["height"])

print()

if artist == "":
    print("Nothing is playing right now.")
else:
    print(
        f" >>> Currently playing {artist} - {track} from the album {album} on {deviceName}.\n"
    )
    dl_album(albumArt, "E:\Documents\Documents\Python\TestApp", "cover")
    # fileName = track + albumArtSize + ".jpg"
    # colors = colorgram.extract("cover.jpg", 6)
    # palette = list(colors.rgb)
    color_thief = ColorThief("cover.jpg")
    palette = color_thief.get_palette(color_count=6)
    print(palette)
    print(type(palette))
    print(f" >>>  palettes--{palette}")

    print()
    # colours = [list(i) for i in palette]

    # arr = []
    # x = 0
    # while True:
    #     colr_no = secrets.randbelow(6)
    #     x = x + 1
    #     for i in range(50):
    #         arr.append(
    #             [i, colours[colr_no][0], colours[colr_no][1], colours[colr_no][2]]
    #         )
    #     bar_sender(arr, x)
    #     time.sleep(3)

