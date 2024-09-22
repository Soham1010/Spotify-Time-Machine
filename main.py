import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from billboard import Billboard
import os 
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file




scope = "playlist-modify-private playlist-read-private playlist-modify-public"
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
ID = os.getenv('ID')


DISPLAY_NAME = 'Wattswade'

API_BASE_URL = 'https://api.spotify.com/v1/'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="https://example.com/"),)
print(sp)

board = Billboard()
date = board.date
billboard_songs = list(board.song_names())


# Create playlist and get its id
new_playlist = sp.user_playlist_create(user=ID, name=f"{date} Billboard 100", public=True, collaborative=False, description="tis amahat, and now here.")
new_playlist_id = new_playlist['id']



##---------------------------------------------------------
# Search query in spotify
year = date[:4]


billboard_songs_uri = []
for song in billboard_songs:
    query = f'track: {song} year: {year}'
    track_search = sp.search(query, limit=5, offset=0, type='track', market=None)

    try:
        uri = track_search["tracks"]["items"][0]["uri"]
        billboard_songs_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


sp.playlist_add_items(playlist_id=new_playlist["id"], items=billboard_songs_uri)






 



