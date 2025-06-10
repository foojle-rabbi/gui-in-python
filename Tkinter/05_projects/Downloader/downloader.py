import yt_dlp
import re
import unicodedata


# ----- mehotds to clear the title ------------
def clean_title(title: str) -> str:
    # Normalize Unicode to ASCII
    normalized = unicodedata.normalize('NFKD', title).encode('ASCII', 'ignore').decode('ASCII')
    # Remove any character that is NOT a letter, number, space, dash, or underscore
    cleaned = re.sub(r'[^A-Za-z0-9 _-]', '', normalized)
    # Replace spaces with underscores (optional, safer for filenames)
    cleaned = cleaned.replace(' ', '_')
    # Optional: limit length (e.g., max 100 chars)
    return cleaned[:100]

while(1):
    download_folder = r"C:\Users\Fojle Rabbi\Downloads"
    url = input("Enter the URL: ")

    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'video')
        safe_title = clean_title(title)
        
        ydl_opts = {
            'outtmpl': f"{download_folder}/{safe_title}.%(ext)s",  # use safe_title here
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])