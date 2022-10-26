from pytube import YouTube
import os

def get_video(yt:str):
    yt = YouTube(yt)
    yt = yt.streams.filter(only_video=True)
    current_directory = os.getcwd()
    end_directory = "\Downloads\Videos"
    current_directory.replace("\dist", "")
    end_directory = current_directory + end_directory
    yt.first().download(end_directory)

def get_audio(yt:str):
    yt = YouTube(yt)
    yt = yt.streams.filter(only_audio=True)
    yt.first().download(".\Downloads\Audios")