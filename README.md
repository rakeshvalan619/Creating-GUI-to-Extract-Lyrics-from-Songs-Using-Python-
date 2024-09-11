# INTRODUCTION

This documentation provides a clear and concise explanation of the Lyrics Fetcher application. The application is built using Python and the `tkinter` library for the graphical user interface (GUI). It integrates with the Genius API, using the `lyricsgenius` library, to fetch and display song lyrics based on the artist and song name provided by the user.

## PREREQUISITES

1. **Python 3.12.2**
2. **Required Libraries: `tkinter` and `lyricsgenius`**

### 1. `lyricsgenius`
A library to interact with the Genius API to fetch lyrics for the given song.

### 2. `tkinter`
A standard GUI library in Python which is used to create the GUI interface for our code.

### 3. `messagebox`
A module in `tkinter` to show message boxes.

## GENIUS

It is used to initialize the Genius API client with my access token, and I used that access token in my program to connect with the Genius server.

### Code Snippets:

- **`artist = artist_entry.get()`**: Retrieves the artist name from the input field.
- **`song = song_entry.get()`**: Retrieves the song name from the input field filled by the end user.
- **`genius.search_song(song, artist)`**: Searches for the song lyrics using the Genius API.
- **`lyrics_text.delete("1.0", tk.END)`**: Clears the previous details of the lyrics entered by the user.
- **`lyrics_text.insert(tk.END, song_data.lyrics)`**: Inserts the fetched lyrics into the text area.
- **`messagebox.showerror`**: Displays an error message if the song is not found or if any error occurs.
- **`messagebox.showwarning`**: If either the artist's name or song name is not entered, it displays a warning message.

## GUI DETAILS

- **`root = tk.Tk()`**: Initializes the main window.
- **`root.title("Lyrics Fetcher")`**: Sets the title of the window to "Lyrics Fetcher".
- **`root.geometry("600x400")`**: Sets the dimensions of the window to 600x400.

### Widgets:

- **`tk.Label`**: Creates labels for the artist and song input fields.
- **`tk.Entry`**: Creates input fields for the artist and song names.
  - **`pack(pady=5)`**: Adds padding around the widgets for better spacing.
- **`tk.Button`**: Creates a button that calls the `fetch_lyrics` function when clicked.
  - **`command=fetch_lyrics`**: Binds the button click event to the `fetch_lyrics` function.
  - **`pack(pady=10)`**: Adds padding around the button.
- **`tk.Text`**: Creates a text area to display the fetched lyrics.
  - **`wrap='word'`**: Wraps text at word boundaries.
  - **`height=15, width=60`**: Sets the dimensions of the text area.
  - **`pack(pady=10)`**: Adds padding around the text area.

## EVENT LOOP

- **`root.mainloop()`**: Starts the main event loop, which waits for user interaction and updates the GUI accordingly.

## RUN THE SCRIPT

Running the script will open a window where you can enter the artist's name and the song title to fetch and display the lyrics.

# CONCLUSION

This application allows users to fetch song lyrics by entering the artist's name and the song title. The `tkinter` library is used to create a user-friendly GUI, and the `lyricsgenius` library interacts with the Genius API to retrieve the lyrics.
