# spotify-playlist-downloader - Downloading Spotify Playlists

From Playlist ID:
```
python main.py -p PLAYLIST_SPOTIFY_ID -d DIRECTORY
```

From Playlist URI:
```
python main.py -u PLAYLIST_SPOTIFY_URI -d DIRECTORY
```


## Example

![Screenshot](https://i.imgur.com/bhLmsh8.png)



Result:

![Screenshot](https://i.imgur.com/EzNTbPx.png)


--------------------------------------------------

## Steps / Requirements

#### 1) Get your own CLIENT_ID and SECRET_ID

You can visit the official page (https://developer.spotify.com/documentation/general/guides/authorization-guide/) or follow these instructions:

- Visit and log into: https://developer.spotify.com/dashboard/applications

Set your CLIENT_ID and SECRET_ID in the `config.py` file, see the [example](https://github.com/chess-seventh/spotify-playlist-downloader/blob/master/config.example.py).


#### 2.a) Get the Playlist ID if using web client...

![Screenshot](https://i.imgur.com/70VDD4K.png)



#### 2.b) ...or get the Playlist URI if using heavy client

![Screenshot](https://i.imgur.com/YliDKpR.png)




#### 3) Install dependencies


Works better with Python 3.5+

Python 3.x:

```
pip3 install -r requirements.txt
```

-----------------------------

## Authors

- [@Javisalva9](https://github.com/Javisalva9)

- [@ricardojoserf](https://github.com/ricardojoserf)

- [@chess7th](https://github.com/chess-seventh)

## Note

Tested both in Python2.x (2.7.15rc1) and Python 3.x (3.6.7)
