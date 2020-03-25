import time
import json

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

import settings.settings as settings

if __name__ == "__main__":
    # sp = spotipy.Spotify(
    #     client_credentials_manager=SpotifyClientCredentials(
    #         settings.SPOTIFY['client_id'],
    #         settings.SPOTIFY['client_secret']
    #     )
    # )

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

    res = sp.devices()
    print(res)

    # Change track
    sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])

