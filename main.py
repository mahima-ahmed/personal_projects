import os #library that interacts with the operating system
import pygame #library for creating video games
import tkinter as tk #library for creating graphical user interfaces
from tkinter import filedialog #module for displaying message boxes in tkinter
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide' #hide pygame support prompt

# ---------- PYGAME ----------
try:
    pygame.mixer.init() #pygame module for loading and playing sounds
except pygame.error as e: #error handling represented by 'e'
    print('Audio initialization failed! ', e)
    exit()

music_folder = filedialog.askdirectory(title="Select your music folder") #select a music folder

if not os.path.isdir(music_folder):  #check if the music folder exists or not
    print(f'Music folder "{music_folder}" not found!') #print message if folder does not exist
    exit()

mp3_files = [file for file in os.listdir(music_folder) if file.endswith('.mp3')] #list all the files within the music folder and check if they are in mp3 format

if not mp3_files: #check if there are no mp3 files in the folder
    print(f'No mp3 files found in "{music_folder}" folder!') #print message if no mp3 files are found
    exit()

current_music = None #variable to keep track of the currently playing music

# ---------- MUSIC FUNCTIONS ----------
def play_music():
    global current_music #declare current_music as a global variable
    selection = song_listbox.curselection() #get the selected item from the listbox

    if not selection: #check if no item is selected
        messagebox.showwarning('No selection', 'Please select a song to play.') #show warning message
        return

    current_music = mp3_files[selection[0]] #get the selected song from the listbox
    file_path = os.path.join(music_folder, current_music) #connect folder path and song name

    pygame.mixer.music.load(file_path) #load the music file
    pygame.mixer.music.play() #play the loaded music file
    print(f'Now playing: {current_music}') #print the name of the song being played

# ---------- Main Programme ----------
def pause_music():
    pygame.mixer.music.pause() #pause the music
    status_label.config(text='Paused') #update status label
def resume_music():
    pygame.mixer.music.unpause() #resume the music
    status_label.config(text='Resumed') #update status label
def stop_music():
    pygame.mixer.music.stop() #stop the music
    status_label.config(text='Stopped') #update status label
def choose_new_folder():
    global music_folder, mp3_files #declare music_folder and mp3_files as global variables
    music_folder = filedialog.askdirectory(title="Select your music folder") #select a new music folder

    if not os.path.isdir(music_folder):  #check if the new music folder exists or not
        print(f'Music folder "{music_folder}" not found!') #print message if folder does not exist
        return

    music_folder = filedialog.askdirectory(title="Select your music folder") #select a music folder
    mp3_files = [file for file in os.listdir(music_folder) if file.endswith('.mp3')] #list all the files within the new music folder and check if they are in mp3 format

    if not mp3_files: #check if there are no mp3 files in the new folder
        print(f'No mp3 files found in "{music_folder}" folder!') #print message if no mp3 files are found
        return

    song_listbox.delete(0, tk.END) #clear the current listbox
    for song in mp3_files: #loop through each song in the new mp3_files list
        song_listbox.insert(tk.END, song) #insert each song into the listbox

# ---------- GUI ----------
bg_color = '#FEC5E5'
btn_color = '#E17F93'
root = tk.Tk() #create the main window
root.title('Music Player') #set the title of the window
root.geometry('450x450') #set the size of the window
root.resizable(True, True) #make the window non-resizable
root.config(bg= bg_color) #set the background color of the window
root.config(highlightbackground= btn_color) #set the highlight background color of the window

title_label = tk.Label(
    root,
    text='🌷 Music Player 🌷',
    font=('ComicSans', 16, 'bold'),
    fg= '#E11584',
    bg = bg_color
)#create title label
title_label.pack(pady=10) #add padding to the title label

song_listbox = tk.Listbox(
    root,
    width=60,
    height=8,
    bg= '#FEC5E5',
    fg= '#F25278',
    font= ('Cousine', 10, 'bold')
) #create a listbox to display songs
song_listbox.pack(pady=10) #add padding to the listbox

for song in mp3_files: #loop through each song in the mp3_files list
    song_listbox.insert(tk.END, song) #insert each song into the listbox

button_frame = tk.Frame(root, bg=bg_color) #create a frame for buttons
button_frame.pack(pady=10) #add padding to the button frame

play_button = tk.Button(button_frame, text="▶ Play", width=10, bg= btn_color, command=play_music) #create play button
play_button.grid(row=0, column=0, padx=5) #position play button

pause_button = tk.Button(button_frame, text="⏸ Pause", width=10, bg= btn_color, command=pause_music) #create pause button
pause_button.grid(row=0, column=1, padx=5) #position pause button

resume_button = tk.Button(button_frame, text="▶ Resume", width=10, bg= btn_color, command=resume_music) #create resume button
resume_button.grid(row=1, column=0, padx=5, pady= 5) #position resume button

stop_button = tk.Button(button_frame, text="■ Stop", width=10, bg= btn_color, command=stop_music) #create stop button
stop_button.grid(row=1, column=1, padx=5, pady=5) #position stop button

change_folder_button = tk.Button(root, text="📁 Change Folder", width=20, bg= btn_color, command=choose_new_folder) #create change folder button
change_folder_button.pack(pady=10) #add padding to the change folder button

status_label = tk.Label(root, text='Select a song to play', font=('Cousine', 11), fg= '#E11584') #create status label
status_label.pack(pady=10) #add padding to the status label

root.mainloop() #start the main event loop of the GUI