from pytube import YouTube
import os

def get_video(yt:str):
    yt = YouTube(yt)
    yt = yt.streams.filter(file_extension="mp4")
    yt.get_highest_resolution().download()

def get_audio(yt:str):
    yt = YouTube(yt)
    yt = yt.streams.filter(type="audio")
    yt.first().download()