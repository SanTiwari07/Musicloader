import streamlit as st
from downloader import download_youtube
from spotify_to_youtube import spotify_to_ytsearch

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MusicLoader",
    page_icon="🎵",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 4rem;
        margin-bottom: 0;
        font-weight: 700;
    }
    .subtitle {
        text-align: center;
        color: gray;
        margin-top: 0;
        font-size: 1.3rem;
    }
    .stButton button {
        font-weight: 600;
        font-size: 1.1rem;
        padding: 0.75rem 1.5rem;
    }
    .stTextInput input {
        font-size: 1.1rem;
        padding: 0.75rem;
    }
    .stSelectbox select {
        font-size: 1.1rem;
        padding: 0.75rem;
    }
    h3 {
        font-size: 1.5rem;
    }
    .stAlert {
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 class='main-title'>🎵 MusicLoader</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Download music or videos from YouTube & Spotify</p>", unsafe_allow_html=True)
st.divider()

# ---------------- SESSION STATE INIT ----------------
if "done" not in st.session_state:
    st.session_state.done = False
if "url" not in st.session_state:
    st.session_state.url = ""

# ---------------- HELPER FUNCTIONS ----------------
@st.cache_data(show_spinner=False)
def process_spotify_url(spotify_url):
    """Cache Spotify to YouTube conversions"""
    return spotify_to_ytsearch(spotify_url)

def is_valid_url(url):
    """Validate URL format"""
    return url and ("youtube.com" in url or "youtu.be" in url or "spotify.com" in url)

def reset_state():
    """Reset app state"""
    st.session_state.done = False
    st.session_state.url = ""

# ---------------- MAIN APP ----------------
if not st.session_state.done:
    # Input section
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 🔗 Paste your link")
        url = st.text_input(
            "YouTube or Spotify link",
            placeholder="https://www.youtube.com/... or https://open.spotify.com/track/...",
            key="url_input",
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("### 🎧 Format")
        file_type = st.selectbox(
            "Format",
            ["mp3", "mp4"],
            label_visibility="collapsed"
        )
    
    st.divider()
    
    # Download button
    if st.button("⬇️ Download", use_container_width=True, type="primary"):
        if not is_valid_url(url):
            st.error("⚠️ Please paste a valid YouTube or Spotify link.")
        else:
            st.session_state.url = url
            
            with st.spinner("🔄 Processing your request..."):
                try:
                    # Process URL
                    if "spotify.com" in url:
                        query = process_spotify_url(url)
                    else:
                        query = url
                    
                    # Download
                    result = download_youtube(query, file_type)
                    
                    if result is True:
                        st.session_state.done = True
                        st.rerun()
                    else:
                        st.error(f"❌ Download failed: {result}")
                
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")

else:
    # Success state
    st.success("✅ Download completed successfully!")
    st.info(f"📁 Downloaded from: {st.session_state.url[:50]}..." if len(st.session_state.url) > 50 else f"📁 Downloaded from: {st.session_state.url}")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎵 Download Another", use_container_width=True, type="primary"):
            reset_state()
            st.rerun()
    
    with col2:
        if st.button("🔄 Clear", use_container_width=True):
            reset_state()
            st.rerun()

# ---------------- FOOTER ----------------
st.divider()
st.markdown(
    "<p style='text-align: center; font-size: 12px; color: gray;'>"
    "Built with ❤️ using Python & Streamlit<br>"
    "For educational and personal use only"
    "</p>",
    unsafe_allow_html=True
)