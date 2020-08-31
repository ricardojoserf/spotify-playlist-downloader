# spotify-playlist-downloader - Downloading Spotify Playlists

From Playlist ID:
```
python3 main.py -p PLAYLIST_SPOTIFY_ID -i CLIENT_ID -s CLIENT_SECRET [-d OUTPUT_DIRECTORY]
```

From Playlist URI:
```
python3 main.py -u PLAYLIST_SPOTIFY_URI -i CLIENT_ID -s CLIENT_SECRET [-d OUTPUT_DIRECTORY]
```


--------------------------------------------------


## Example

```
python3 main.py -p 0AFu117j8WX2auNWDAyMMV -i $CLIENT_ID -s $CLIENT_SECRET -d playlist_id_example_output

python3 main.py -u spotify:playlist:0AFu117j8WX2auNWDAyMMV -i $CLIENT_ID -s $CLIENT_SECRET -d uri_example_output
```

![Screenshot](https://i.imgur.com/6DyO0Tz.jpg)


Result:

![Screenshot](https://i.imgur.com/EzNTbPx.png)


--------------------------------------------------


## Steps & Requirements

#### 1) Get your own CLIENT_ID and SECRET_ID

You can visit the official page (https://developer.spotify.com/documentation/general/guides/authorization-guide/) or follow these instructions:

- Visit and log into: https://developer.spotify.com/dashboard/applications

- Create a test application and get the "Client ID" and "Client Secret" values. Use them with the paramaters "-i" and "-s"


#### 2.a) Get the Playlist ID if using web client...

![Screenshot](https://i.imgur.com/70VDD4K.png)


#### 2.b) ...or get the Playlist URI if using heavy client

![Screenshot](https://i.imgur.com/YliDKpR.png)


#### 3) Install dependencies

```
apt install ffmpeg

pip3 install -r requirements.txt
```

-----------------------------

## Authors

- [@Javisalva9](https://github.com/Javisalva9)

- [@ricardojoserf](https://github.com/ricardojoserf)

- [@chess7th](https://github.com/chess-seventh)


## Note

Only working with Python 3.x (tested using 3.8.1).
