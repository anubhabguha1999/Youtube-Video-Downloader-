from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
import shutil


#Functions
def select_video_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def select_playlist_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_labelPL.config(text=path)

def download_video():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another Video...')

def download_playlist():
    #get user path
    get_link = link_fieldPL.get()
    #get selected path
    user_path = path_labelPL.cget("text")
    screen.title('Downloading...')
    #Download Playlist
    mp4_video = Playlist(get_link)
    for video in mp4_video.videos:
        vid = video.streams.get_highest_resolution().download()
        #move file to selected directory
        shutil.move(vid, user_path)
    screen.title('Download Complete! Download Another Playlist...')

screen = Tk()
title = screen.title('Youtube Video Downloader')
canvas = Canvas(screen, width=500, height=800)
canvas.pack()

#image logo
#logo_img = PhotoImage(file='Utube.png')
#resize
#logo_img = logo_img.subsample(2, 2)
#canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Video Link Below: ", font=('Arial', 15))


link_fieldPL = Entry(screen, width=40, font=('Arial', 15) )
link_labelPL = Label(screen, text="Enter Playlist Link Below: ", font=('Arial', 15))


#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='crimson', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_video_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

canvas.create_window(250, 460, window=link_labelPL)
canvas.create_window(250, 510, window=link_fieldPL)

#Download btns
download_btn = Button(screen, text="Download Video",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_video)
#add to canvas
canvas.create_window(250, 390, window=download_btn)

path_labelPL = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btnPL =  Button(screen, text="Select Path", bg='crimson', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_playlist_path)
#Add to window
canvas.create_window(250, 580, window=path_labelPL)
canvas.create_window(250, 630, window=select_btnPL)

#Download btns
download_btnPL = Button(screen, text="Download Video",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_playlist)
#add to canvas
canvas.create_window(250, 690, window=download_btnPL)

screen.mainloop()