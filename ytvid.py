import tkinter
import customtkinter
from pytube import YouTube


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("720x480")
app.title("codename : azuki")

title = customtkinter.CTkLabel(app, text = "Please enter a youtube link to download it locally")
title.pack(padx= 40, pady = 40)

urlstring = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=450, height=50, textvariable=urlstring)
link.pack()

def download():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink)
        video = ytobject.streams.get_highest_resolution()
        video.download(output_path='/home/saru/Videos')

    except:
        print("error happened")
    finish_label.configure(text-"Download Completed")

download = customtkinter.CTkButton(app, text="Download", command=download)
download.pack(padx=10, pady=10)

finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()
app.mainloop()