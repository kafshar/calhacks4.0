import spotipy
import spotipy.util as util
token = util.prompt_for_user_token('1267938772','user-library-modify',client_id='ca09ab003299448ab17d3fffd5aaa141',client_secret='e74a619414dd4fadbd6b47f7b73b9d88',redirect_uri='http://localhost:8888/callback/')
name = 'Kanye West'
spotify = spotipy.Spotify(auth=token)
results = spotify.search(q='artist:' + name, type='artist')
print(results)

# import spotipy
#
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify()
#
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])
