from spotify_utils import get_spotify_track_info

url = "https://open.spotify.com/track/34lfu3S4fIcKZRNXzbdbo7?si=7c04648a59574b7f"

song, artist = get_spotify_track_info(url)
print(song, "-", artist)
