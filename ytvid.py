import tkinter
import customtkinter
from pytube import YouTube
import os
from pathlib import Path

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.geometry("720x480")
app.title("codename : azuki")

title = customtkinter.CTkLabel(app, text = "Please enter a youtube link to download it locally")
title.pack(padx= 40, pady = 40)

urlstring = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=450, height=40, textvariable=urlstring, corner_radius=20)
link.pack(padx=5, pady=5)

def download():
    try:
        progressBar.pack(padx=20, pady=20)
        progressBar.set(0)
        pPercentage.pack(padx=20, pady=20)
        ytlink = link.get()
        ytobject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytobject.streams.get_highest_resolution()
        video.download(output_path=str(os.path.join(Path.home(), 'Downloads')))

    except:
        print("error happened")
    finish_label.configure(text="Download Completed")

pPercentage = customtkinter.CTkLabel(app, text="0%",font=('SF Pro Display',16))


progressBar = customtkinter.CTkProgressBar(app, width =350, height=15)


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size *100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_completion) / 100)

download = customtkinter.CTkButton(app, text="Download", command=download, corner_radius=30)
download.pack(padx=30, pady=30)

finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()
app.mainloop()