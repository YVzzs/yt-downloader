from tkinter import *
from pytube import YouTube
import os

window =Tk()
window.geometry("600x700")
window.config(bg = "red")
window.title("YOUTUBE SUPER DOWNLOADER BY YAVUZ")



Label(window, text = " Super YouTube Downloader", font=("Arial 30 bold"), bg="gray").pack(padx=5, pady=50)

video_link = StringVar()

Label(window, text="Enter the link : ", font=("Arial",25,"bold")).place(x=170, y=150)
Entry_link=Entry(window, width=50, font=35, textvariable=video_link, bd=4).place(x=35,y=200)

def mp4_download():
    video_url = YouTube (str(video_link.get()))
    videos=video_url.streams.get_highest_resolution().download()

    Label(window, text="Download Completed !!", font=("Arial", 25,"bold"),bg="lightpink", fg="black").place(x=120,y=375)

Button(window,text="DOWNLOAD MP4", font=("Arial",25,"bold"),bg="purple", command=mp4_download).place(x=180,y=450)

def mp3_download():
    video_url = YouTube (str(video_link.get()))
    videos=video_url.streams.filter(only_audio=True).first().download()

    base, ext = os.path.splitext(videos)
    new_file = base + '.mp3'
    os.rename(videos, new_file)
    

    Label(window, text="Download Completed !!", font=("Arial", 25,"bold"),bg="lightpink", fg="black").place(x=120,y=375)
   
Button(window,text="DOWNLOAD MP3", font=("Arial",25,"bold"),bg="blue", command=mp3_download).place(x=180,y=300)    
     

window.mainloop()