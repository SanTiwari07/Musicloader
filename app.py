import streamlit as st
from downloader import download_youtube
from spotify_to_youtube import spotify_to_ytsearch

st.title("🎵 MusicLoader")

url = st.text_input("Enter YouTube or Spotify link")
file_type = st.radio("Select format", ["mp3", "mp4"])

if st.button("Download"):
    if not url:
        st.error("Please enter a link")
    else:
        st.success("Processing...")

        if "spotify.com" in url:
            query = spotify_to_ytsearch(url)
        else:
            query = url  # YouTube link directly

        result = download_youtube(query, file_type)

        if result is True:
            st.success("Download completed 🎉")
        else:
            st.error(result)
