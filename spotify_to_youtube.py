from spotify_utils import get_spotify_track_info

def spotify_to_ytsearch(spotify_url):
    song, artist = get_spotify_track_info(spotify_url)
    return f"ytsearch1:{song} {artist}"
