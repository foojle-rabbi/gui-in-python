# now lets make a downloader with GUI interface
import tkinter as tk
from tkinter import messagebox
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

def on_click():
    url = text_box.get("1.0", "end-1c")

    if not url:
        messagebox.showwarning("Warnings", "Enter a Valid URL")
        return
    # now as we got the url lets do our works
    
    # the saving path
    download_folder = r"C:\Users\Fojle Rabbi\Downloads"

    # lefts first do some settings
    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'video')
        safe_title = clean_title(title)
        
        ydl_opts = {
            'outtmpl': f"{download_folder}/{safe_title}.%(ext)s",  # use safe_title here
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
    # now clear the inputs texts
    text_box.delete("1.0", "end")

# Main window
root = tk.Tk()
root.geometry("450x200")
root.title("Downloader")
root.resizable(False, False)

# now lets add a label
enter_url = tk.Label(root, text="Enter the Url: ")
text_box = tk.Text(root, height=2, width=35)

# download button:
download_btn = tk.Button(root, text="Download", command=on_click)

# packing methods
enter_url.pack()
text_box.pack()
download_btn.pack()

root.mainloop()