import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='a3d608b405554a9a9735da2be6e12f08', client_secret='76727e6600c2436f92b6a59833c0703b')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def give_keyword(keyword):
    playlists = sp.search(q=keyword, type='playlist')
    artist = sp.artist('339DNkQkuhHKEcHw6oK8f0')
    print(playlists['playlists']['items'][0]['uri'])
    print(playlists['playlists']['items'][0]['name'])
