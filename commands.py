from pytube import YouTube
import os

def get_video(yt:str):
    yt = YouTube(yt)
    yt = yt.streams.filter(only_video=True)
    current_directory = os.getcwd()
    current_directory = current_directory.replace("\dist", "\Downloads\Videos")
    end_directory = os.chdir(current_directory)
    yt.first().download()

def get_audio(yt:str):
    yt = YouTube(yt)
    yt = yt.streams.get_audio_only()
    current_directory = os.getcwd()
    current_directory = current_directory.replace("\dist", "\Downloads\Audios")
    end_directory = os.chdir(current_directory)
    yt.first().download()