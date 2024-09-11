import lyricsgenius

import tkinter as tk
from tkinter import messagebox
import lyricsgenius

genius = lyricsgenius.Genius('EyIK8LfBc1Jr3Urud8kGv9qA-MbA_hJjFW9Qz1scxgTkYrDcQlj8VMeulbRl9Xql')

def fetch_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()
    
    if artist and song:
        try:
            song_data = genius.search_song(song, artist)
            if song_data:
                lyrics_text.delete("1.0", tk.END)
                lyrics_text.insert(tk.END, song_data.lyrics)
            else:
                messagebox.showerror("Error", "Song not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter both artist and song name")

root = tk.Tk()
root.title("Lyrics Fetcher")
root.geometry("600x400")

artist_label = tk.Label(root, text="Artist Name")
artist_label.pack(pady=5)
artist_entry = tk.Entry(root, width=50)
artist_entry.pack(pady=5)

song_label = tk.Label(root, text="Song Name")
song_label.pack(pady=5)
song_entry = tk.Entry(root, width=50)
song_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.pack(pady=10)

lyrics_text = tk.Text(root, wrap='word', height=15, width=60)
lyrics_text.pack(pady=10)

root.mainloop()
