from pytube import YouTube
import os

def get_video(yt:str):
    yt = YouTube(yt)
    yt = yt.streams.filter(only_video=True)
    yt.first().download("./Downloads/Videos")

def get_audio(yt:str):
    yt = YouTube(yt)
    yt = yt.streams.filter(only_audio=True)
    yt.first().download("./Downloads/Audios")