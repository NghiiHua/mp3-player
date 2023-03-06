import tkinter as tk
from tkinter import filedialog
import vlc # install vlc package
import os
# os.path: https://stackoverflow.com/questions/3315045/remove-last-path-component-in-a-string
import os.path

root = tk.Tk()
root.title("MP3 Player")
root.geometry("290x310")

global media
media = vlc.MediaPlayer()

# all songs
global list
list = []

def submit():
    global rename
    rename = data.get()
    placeholder = str(temp + "/" + rename + ".mp3")
    os.rename(str(song_name), placeholder) # change path name
    # debug: print(song_name)

    playlist.insert("end", rename) # add to end of Listbox "playlist"
    list.append(str(placeholder))
    # debug: print(song_name)
    # debug: print(list)

def addsongs():
    global song_name
    global data
    global temp

    # askopenfilenames returns file name
    song_name = tk.filedialog.askopenfilenames(filetypes=(("mp3 Files", "*.mp3"),))
    song_name = song_name[-1] # delete "," at the end
    # os.dirname: https://stackoverflow.com/questions/3315045/remove-last-path-component-in-a-string
    temp = os.path.dirname(str(song_name)) # remove last path

    # get user input on tkinter
    data = tk.Entry(root)
    data.focus_set()
    data.grid(row=4, column=1)
    tk.Label(text="Song Name - Artist: ").grid(row=3, column=1)
    tk.Button(root, text="Submit", command=lambda: submit()).grid(row=5, column=1)

# source: https://www.geeksforgeeks.org/python-vlc-mediaplayer-pausing-it/
def pause():
    song.stop()

# source: VLC intro. - https://www.youtube.com/watch?v=WK8q4z1HBHM
def play():
    global song
    # debug: print(song_name)
    for item in playlist.curselection():
        song = vlc.MediaPlayer(f"{list[item]}")
        pause()
        # debug: print(list[item])
    song.play()

def skip():
    global song
    pause()
    for item in playlist.curselection():
        if item != list[-1]:
            song = vlc.MediaPlayer(f"{list[item+1]}")
        # debug: print(list[item])
    song.play()

def prev():
    global song
    pause()
    for item in playlist.curselection():
        if list.index(list[item]) != 0:
            song = vlc.MediaPlayer(f"{list[item-1]}")
    song.play()

def options(i):
    if i == 0:
        play()
    elif i == 1:
        pause()
    elif i == 2:
        skip()
    else:
        prev()

# create playlist
# Listbox: https://www.geeksforgeeks.org/python-tkinter-listbox-widget/
tk.Label(text="PLAYLIST").grid(row=0, column=1)
playlist = tk.Listbox(root)
playlist.grid(row=1, column=1)

# button to add song
add = tk.Button(root, text="Add Song", command=lambda: addsongs()).grid(
    row=2, column=1)

# create functions buttons
functions = ["Play", "Pause", "Skip", "Prev"]
x = 0
row = 2
for i in range(len(functions)):
    tk.Button(root, text=functions[i], command=lambda i=i: options(i)).grid(
        row=row, column=0, sticky="nesw")
    x += 1
    row += 1

root.mainloop()