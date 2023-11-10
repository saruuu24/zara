import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("720x480")
app.title("azuki")

title = customtkinter.CTkLabel(app, text = "Please enter a youtube link to download it locally")
title.pack(padx= 40, pady = 40)

link = customtkinter.CTkEntry(app, width=450, height=50)
link.pack()
app.mainloop()