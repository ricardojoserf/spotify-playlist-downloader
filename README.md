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

#### 1) Get your own access token 

You can visit the official page (https://developer.spotify.com/documentation/general/guides/authorization-guide/) or follow these instructions:

- Visit and log into: https://developer.spotify.com/dashboard/applications

- Create a "test" application

- Click "Edit settings" and add "https://example.com/callback/" as "Redirect URIs". Save changes

- Copy your "Client ID" value

- Replace "CLIENT_ID" with your own value and visit 
```
https://accounts.spotify.com/authorize?client_id=**CLIENT_ID**&redirect_uri=https:%2F%2Fexample.com%2Fcallback/&scope=user-read-private%20user-read-email&response_type=token&state=123
```

- Click "Accept" and extract your access token from the url:
```
http://example.com/callback/#access_token=**ACCESS_TOKEN**&token_type=Bearer&expires_in=3600&state=123
```


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
