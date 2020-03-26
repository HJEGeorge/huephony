import json
import time
from itertools import cycle

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

import settings.settings as settings


import requests
from phue import Bridge

#%%

from datatypes.datatypes import Hue, Brightness, ColorTemp


if __name__ == "__main__":
    # sp = spotipy.Spotify(
    #     client_credentials_manager=SpotifyClientCredentials(
    #         settings.SPOTIFY['client_id'],
    #         settings.SPOTIFY['client_secret']
    #     )
    # )

    print('Authenticating Spotify...')
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(
        client_credentials_manager=
            SpotifyOAuth(
                scope=scope,
                client_id=settings.SPOTIFY['client_id'],
                client_secret=settings.SPOTIFY['client_secret'],
                redirect_uri='http://localhost:8080/callback',
                username='hjegeorge@gmail.com'
            )
    )
    print("Authentication complete :)")

    devices_response = sp.devices()
    print('Connected Spotify Devices:')
    for device in devices_response['devices']:
        print(f"{device['name']} ({device['type']}), Volume: {device['volume_percent']}%, Active: {device['is_active']}")
    if not devices_response['devices']:
        print('Could not find any devices, please open Spotify on at least one device')

    print("Connecting to Hue Bridge...")

    HUE_DISCOVER = 'http://discovery.meethue.com'

    response = requests.request('GET', HUE_DISCOVER)
    bridges = json.loads(response.content)
    bridge_ip = bridges[0]['internalipaddress']
    bridge = Bridge(bridge_ip)
    bridge.connect()
    if bridge:
        print("Connection to Hue Bridge successful :)")
    else:
        print("connection to Hue unsuccessful, please try pressing the button on your bridge.")
    
    time.sleep(1)
    print("Let's boogie")

    # Prep lights
    print("Light choices are:")
    lights = bridge.get_light_objects('name')
    for idx, key in enumerate(lights.keys()):
        print(f" ({idx}) {key}  ")
    if not lights.keys():
        print('Turn yo fuckin lights on you rookie')


    choice = input(f"Which light you wanna boogie wiv? (Enter the name) (default: {key})")

    light = lights[choice or key]

    colours = cycle([Hue.BLUE.value, Hue.RED.value])
    light.transitiontime = 0

    song_query = input("Which song you wanna boogie to? (will choose the closest match) (default: Daft Punk - Around the World)")
    if not song_query:
        song_query = "Daft Punk Around the world"
    song = sp.search(q=song_query, limit=1)['tracks']['items'][0]
    song_name = song['name']
    artists = " & ".join([artist['name'] for artist in song['artists']])
    print(f"Playing {song['name']} by {artists}")
    analysis = sp.audio_analysis(song['uri'])
    beats = analysis['beats']
    sp.start_playback(uris=[song['uri']])
    FUDGE_FACTOR = 0.05
    time.sleep(max(analysis['track'].get('end_of_fade_in', 0.4) - FUDGE_FACTOR, 0))
    print("Boogie time")
    for beat in beats:
        light.hue = next(colours)
        time.sleep(beat['duration'])




