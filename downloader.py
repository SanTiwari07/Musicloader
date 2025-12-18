import yt_dlp
import os

def download_youtube(query, file_type):
    try:
        if file_type == "mp3":
            output_folder = "audio"
        else:
            output_folder = "video"

        os.makedirs(output_folder, exist_ok=True)

        ydl_opts = {
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'retries': 10,
            'fragment_retries': 10,
            'socket_timeout': 30,
            'quiet': True,
        }

        if file_type == 'mp3':
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })

        elif file_type == 'mp4':
            ydl_opts.update({
                'format': 'best[ext=mp4]/best',
            })

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([query])

        return True

    except Exception as e:
        return str(e)
