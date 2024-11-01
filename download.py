import yt_dlp

def download_youtube_video_as_mp3(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        
        #download only audio
        'extractaudio': True,

        #save as mp3
        'audioformat': 'mp3',  

        #save file with the original title
        'outtmpl': '%(title)s.%(ext)s', 
        
        #use ffmpeg to convert audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  
            'preferredcodec': 'mp3',
            #audio quality
            'preferredquality': '192',  
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video_as_mp3(video_url)
