# spotify-playlist-downloader - Downloading Spotify Playlists

From Playlist ID:
```
python main.py -a ACCESS_TOKEN -p PLAYLIST_SPOTIFY_ID -d DIRECTORY
```

From Playlist URI:
```
python main.py -a ACCESS_TOKEN -u PLAYLIST_SPOTIFY_URI -d DIRECTORY
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



#### 2.a) Get the Playlist ID if using web client...

![Screenshot](https://i.imgur.com/70VDD4K.png)



#### 2.b) ...or get the Playlist URI if using heavy client

![Screenshot](https://i.imgur.com/YliDKpR.png)




#### 3) Install dependencies


Python 2.x:

```
sudo apt-get install ffmpeg libavcodec-*
pip install instantmusic
```

Python 3.x:

```
sudo apt-get install ffmpeg libavcodec-*
pip3 install instantmusic
```

-----------------------------

## Authors

- [@Javisalva9](https://github.com/Javisalva9)

- [@ricardojoserf](https://github.com/ricardojoserf)

## Note

Tested both in Python2.x (2.7.15rc1) and Python 3.x (3.6.7)
