"""
Spotify Downloader
"""
from __future__ import unicode_literals
import os
import json
import argparse
import youtube_dl
import spotipy
from youtubesearchpython import SearchVideos
from youtube_dl.utils import DownloadError, ExtractorError


def get_args():
    """
    Parse Arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--spotiuri', action='store', help='Playlist\'s  Spotify Uri')
    parser.add_argument('-p', '--spotiplaylistId', action='store', help='Playlist\'s  Spotify id')
    parser.add_argument('-i', '--client_id', required=True, action='store', help='Client\'s id')
    parser.add_argument('-s', '--client_secret', required=True, action='store', help='Client\'s secret')
    parser.add_argument('-d', '--dir_name', required=False, action='store', default="spotify_playlist", help='Directory name')
    my_args = parser.parse_args()

    if not(my_args.spotiuri or my_args.spotiplaylistId):
        parser.error('Need URI or ID')

    return my_args


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
            if not yt_dl(track):
                print(f"This track failed: {wholename}")
                failed.append(f"{song_artist} {song_name}")
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
        'no-playlist': 'True',
        'audio-format': 'best',
        'extract-audio': 'True',
        'addmetadata': 'True',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }]}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([vid])
        except DownloadError as dl_e:
            print(f"Couldn't download: {dl_e}")
            return False
        except ExtractorError as extract_e:
            print(f"Couldn't extract: {extract_e}")
            return False
        return True


def get_yt_link(artist, song):
    """
    Return YT Link to download
    """
    search = SearchVideos(str(artist + " " + song),
                          offset=1,
                          mode="json",
                          max_results=1)
    try:
        return search.links[0]
    except IndexError as e:
        print(f"No videos to download found: {e}")


def main():
    """
    main function
    """
    args = get_args()

    if args.spotiuri:
        playlist_id = args.spotiuri.split(":")[len(args.spotiuri.split(":"))-1]

    if args.spotiplaylistId:
        playlist_id = args.spotiplaylistId

    tok = spotipy.oauth2.SpotifyClientCredentials(client_id=args.client_id,
                                                  client_secret=args.client_secret)

    access_token = tok.get_access_token(as_dict=False)

    result = os.popen('curl -s -X GET "https://api.spotify.com/v1/playlists/'
                      + playlist_id + '/tracks" -H "Authorization: Bearer '
                      + access_token + '"').read()

    dir_name = args.dir_name
    create_dir(dir_name)
    os.chdir(dir_name)
    download_songs(json.loads(result))


if __name__ == "__main__":
    main()