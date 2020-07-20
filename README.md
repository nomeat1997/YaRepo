# Changing the colour of a Mood Light according to a Spotify song

The LEDS (WS2812B, addressable) are connected to a ESP8266 module flashed with WLED.
#https://github.com/Aircoookie/WLED

To get the colours, we use a spotify library called spotipy.
https://github.com/plamere/spotipy

The python script in this repository is used to get the Album Art of the currently playing song.
The album art of this song is processed to get the dominant colours from the album art using library.
https://github.com/lokesh/color-thief

Finally, the dominant colours are uploaded to the ESP8266 module and the colours are set on it.

The script has to be run each time a new song is played.
