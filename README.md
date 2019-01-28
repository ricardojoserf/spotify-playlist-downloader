# spotify-playlist-downloader
Downloading Spotify Playlist

```
python main.py -a ACCESS_TOKEN -u PLAYLIST_SPOTIFY_URI -d DIRECTORY
```


![Screenshot](images/2.png)


![Screenshot](images/3.png)



## Requirements

- Get an access token in https://developer.spotify.com/documentation/general/guides/authorization-guide/

- Get the Playlist URI:


![Screenshot](images/1.png)


- Install dependencies

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

## Note

Tested both in Python2.x (2.7.15rc1) and Python 3.x (3.6.7)