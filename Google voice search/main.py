import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess
import datetime
import webbrowser
import sys
import bs4
import requests


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said =""

        try:
            said = r.recognize_google(audio)
            print('\n', said)
        except Exception as e:
            print("Exception:" +str(e))

    return said

def search(text):
        webbrowser.open('https://www.google.com/search?q='+text+'&rlz=1C1CHBD_enIN913IN913&oq='+text+'&aqs=chrome..69i57j0i13i457j69i60l2j69i61j69i60l2.17119j0j7&sourceid=chrome&ie=UTF-8')

print('start')
text = get_audio().lower()
final_text = text.replace(' ','+')
search(final_text)
