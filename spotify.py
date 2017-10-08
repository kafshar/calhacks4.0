import spotipy
import spotipy.util as util
token = util.prompt_for_user_token('1267938772','user-library-modify',client_id='a3d608b405554a9a9735da2be6e12f08',client_secret='76727e6600c2436f92b6a59833c0703b',redirect_uri='http://localhost/')
#token = 'BQBr2PUnWurUyp1Wq2vYex73YQF9cglRnBiEYC22suHohLPXzjBzFdRM0oA-r2Eq129g50u5dMdnbNr5TvitqiqnIirUBqeNtD2Mzj_CKgY6QQR6CSYOjfEShqjfeEgff2cKIzdBmAxs6BC9eCUdEO-rTP_PKjE&refresh_token=AQC1p7rOI-wW10vwe0mrZi3BUJKdTmpE1wsw0nxtT-ei3OaJ2yqTdqntqZ67grOj7D2SsSYMCnkb8KFM2dO39IKWInMH_NKiZRY2Lt63xm6doBcPUkUmCQWFfzbQr-KfZ-Y'
name = 'happy'
spotify = spotipy.Spotify(auth=token)
results = spotify.search(q='playlist:' + name, type='playlist')
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
