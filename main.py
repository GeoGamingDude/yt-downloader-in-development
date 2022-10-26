import tkinter as tk
from pytube import YouTube
import os
from commands import get_video, get_audio

root = tk.Tk()
root.geometry("400x200")
root.update()

clipboard = root.clipboard_get()

video_or_audio = tk.Label(
    root,
    text="Video or Audio?",
    height=3
)
video_or_audio.pack()

video_button = tk.Button(
    root,
    text="Video",
    width=20,
    height=5,
    command=lambda : get_video(clipboard)
)
video_button.pack()
video_button.place(x=int(245 * .10),y=75)

audio_button = tk.Button(
    root,
    text="Audio",
    width=20,
    height=5,
    command=lambda: get_audio(clipboard)
)
audio_button.pack()
audio_button.place(x=int(245 * .90),y=75)

root.mainloop()