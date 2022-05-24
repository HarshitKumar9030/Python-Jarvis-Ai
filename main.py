import pyttsx3  #pip install pyttsx3
import datetime  #module
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os  #inbuilt
import pyautogui
import psutil  #pip install psutil
import pyjokes  # pip install pyjokes
import requests, json  #inbuilt


engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)


#change voice
def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("Done")

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

    
    
