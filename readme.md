# 🎵 MusicLoader

A Python-based application that allows users to download music and videos offline by providing **Spotify or YouTube links**. Built as a learning project to practice Python fundamentals through hands-on development.

---

## 🚀 Motivation

I love listening to music, but some of my favorite songs are banned or unavailable on certain platforms. Instead of searching for workarounds, I decided to build my own solution while practicing what I learned in Python.

---

## ✨ Features

### YouTube Downloads
- Download audio as **MP3**
- Download video as **MP4**
- Direct link support

### Spotify Downloads
- Extract song metadata (title and artist)
- Automatically search the song on YouTube
- Download audio as **MP3**

### User Interface
- Clean and simple web interface built with **Streamlit**
- Easy-to-use link input
- Real-time download progress

---

## 🧰 Tech Stack

- **Python** - Core programming language
- **Streamlit** - Web interface framework
- **yt-dlp** - YouTube download engine
- **Spotipy** - Spotify Web API wrapper
- **python-dotenv** - Environment variable management

---

## 📁 Project Structure

```
musicloader/
│
├── app.py              # Main Streamlit application
├── config.py           # Configuration settings
├── platform.py         # Platform detection (Spotify/YouTube)
├── downloader.py       # Download logic
├── utils.py            # Helper functions
├── downloads/          # Downloaded files directory
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (not tracked)
└── README.md          # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd musicloader
```

### 2. Create and activate a virtual environment (recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up Spotify API credentials

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Copy your **Client ID** and **Client Secret**
4. Create a `.env` file in the project root:

```env
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 🎯 Usage

1. **Launch the application** using the command above
2. **Paste a link** - Either Spotify or YouTube URL
3. **Select format** - Choose MP3 (audio) or MP4 (video) for YouTube
4. **Click Download** - Files will be saved to the `downloads/` folder

---

## 📌 Disclaimer

⚠️ **Important**: This project is created for **educational purposes only**.

- Downloading copyrighted content may violate the terms of service of content platforms
- This tool should only be used for personal, non-commercial purposes
- Respect artists' rights and support them through official channels
- The developer is not responsible for misuse of this tool

**Please use responsibly.**

---

## 🧠 Learning Outcomes

Through building this project, I practiced:

- ✅ Practical use of Python data structures (tuples, lists, dictionaries)
- ✅ Modular Python programming and project organization
- ✅ Working with external APIs (Spotify Web API)
- ✅ File handling and backend logic
- ✅ Building a web interface with Streamlit
- ✅ Error handling and user input validation
- ✅ Environment variable management
- ✅ Learning by building, not copying

---

## 🔧 Requirements

See `requirements.txt` for full list of dependencies:

```
streamlit
yt-dlp
spotipy
python-dotenv
```

---

## 🤝 Contributing

This is a personal learning project, but suggestions and feedback are welcome! Feel free to:

- Report bugs
- Suggest new features
- Share your learning experience

---

## 📝 License

This project is open source and available for educational purposes.

---

## 👤 Author

**Sanskar**

🚀 Learning Python by building real projects

*"The best way to learn is by doing."*

---

## 🙏 Acknowledgments

- **yt-dlp** - Powerful YouTube download tool
- **Spotipy** - Easy-to-use Spotify API wrapper
- **Streamlit** - Amazing framework for building web apps

---

**Happy Learning! 🎓**