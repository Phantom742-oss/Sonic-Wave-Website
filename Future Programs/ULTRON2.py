import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import subprocess
import webbrowser
import requests
from AppOpener import open

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[0].id)
rate=engine.getProperty("rate")
#print(rate)
engine.setProperty("rate",168)
volume=engine.getProperty("volume")
engine.setProperty("volume",1)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir i'm ULTRON")
        open("Weather")

    elif hour>=12 and hour<16:
        speak("Good Afternoon sir i'm ULTRON how may i help you sir")
        open("Weather")

    elif hour>=16 and hour<20:
        speak("Good Evening Sir i'm ULTRON i hope you have taken your evening snack how may i help you sir  ")
        open("Weather")

    elif hour>=20 and hour<24:
        speak("Sir this your sleeping time what happened and how may i help you")
        open("Weather")

def takecommand():

    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("LISTENING....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing****")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("sorry sir i can't recognise that can you say that again********")
        return "None"
    return query


if  __name__ == "__main__":
    wishme()

    while True :
     query = takecommand()

        
     if "Wikipedia" in query:
            speak("ok sir i'm searching wikipedia for you")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
    
     elif "YouTube" in  query:
        speak("ok sir opening youtube")
        speak("here is your youtube sir enjoy ")
        webbrowser.open("youtube.com")