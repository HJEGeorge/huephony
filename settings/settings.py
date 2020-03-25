import os
from pathlib import Path

from settings.exceptions import IncompleteSettings
from dotenv import load_dotenv

env_path = Path('settings/.env')
load_dotenv(verbose=True, dotenv_path=env_path)

SPOTIFY = {
    'client_id': os.getenv('SPOTIFY_CLIENT_ID'),
    'client_secret': os.getenv('SPOTIFY_CLIENT_SECRET')
}
if SPOTIFY['client_id'] is None:
    raise IncompleteSettings()


