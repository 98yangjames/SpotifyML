import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd


client_id = "7cda6c1856a24d109ba5521fd35fd5a3"
client_secret = "ac6d7cd270aa48cab17e179262d78031"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = "spotify:playlist:6kwZDYZb4nyAVk4PLquWxp"

results = sp.playlist_items(uri)
new = pd.DataFrame.from_dict(results) 

# new.to_csv('output.csv')
df2 = pd.json_normalize(new['items'])
df2.to_csv('output.csv')
