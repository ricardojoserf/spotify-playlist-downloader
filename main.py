"""
Spotify Downloader
"""
from __future__ import unicode_literals
import os
import json
import argparse
from youtubesearchpython import SearchVideos
import youtube_dl
import spotipy
from config import CLIENT_ID
from config import CLIENT_SECRET


def get_args():
    """
    Parse Arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--spotiuri', action='store',
                        help='Playlist\'s  Spotify Uri')
    parser.add_argument('-p', '--spotiplaylistId', action='store',
                        help='Playlist\'s  Spotify id')
    parser.add_argument('-d', '--dir_name', required=True, action='store',
                        help='Directory name')
    my_args = parser.parse_args()

    if not(my_args.spotiuri or my_args.spotiplaylistId):
        parser.error('Need URI or ID')

    return my_args


def changenames(dir_name):
    """
    Fix names of downloaded music.
    """
    songs = [i for i in [s for s in os.listdir("./")
                         if os.path.isfile(os.path.join("./", s))]
             if "mp3" in i]

    count_song = 0
    for song in songs:
        # [''.join(s.split('-')[0:-1]) + ".mp3" for s in songs ]
        count_song += 1
        new_s = f"{count_song:02d}-" + ''.join(song.split('-')[0:-1]) + ".mp3"
        os.rename(os.path.join("./", song), os.path.join(dir_name, new_s))


def create_dir(dir_name):
    """
    Creates dir if it does not exist
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def download_songs(spotify_info):
    """
    Download song
    """
    failed = list()
    print("\nDownloading songs...\n")
    counter = 0
    for item in spotify_info["items"]:
        song_name = item["track"]["artists"][0]["name"]
        song_artist = item["track"]["name"]
        wholename = "%s %s" % (song_name, song_artist)
        counter += 1
        print("%s)\t%s" % (counter, wholename))
        track = get_yt_link(song_artist, song_name)
        if track:
            yt_dl(track)
        else:
            print(f"This track failed: {wholename}")
            failed.append(f"{song_artist} {song_name}")


def yt_dl(vid):
    """
    Download yt music

    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'True',
        'addmetadata': 'True',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([vid])


def get_yt_link(artist, song):
    """
    Returns YT Link to download
    """
    search = SearchVideos(str(artist + " " + song),
                          offset=1,
                          mode="json",
                          max_results=1)
    return search.links[0]


def main():
    """
    main function
    """
    args = get_args()
    dir_name = 'output'

    if args.spotiuri:
        playlist_id = args.spotiuri.split(":")[len(args.spotiuri.split(":"))-1]

    if args.spotiplaylistId:
        playlist_id = args.spotiplaylistId
        dir_name = args.dir_name

    tok = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID,
                                                  client_secret=CLIENT_SECRET)

    access_token = tok.get_access_token(as_dict=False)

    result = os.popen('curl -s -X GET "https://api.spotify.com/v1/playlists/'
                      + playlist_id + '/tracks" -H "Authorization: Bearer '
                      + access_token + '"').read()
    create_dir(dir_name)
    download_songs(json.loads(result))
    changenames(dir_name)


if __name__ == "__main__":
    main()
