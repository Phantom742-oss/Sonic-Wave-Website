import os
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
engine.setProperty("rate",165)
volume=engine.getProperty("volume")
engine.setProperty("volume",1)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir i'm ULTRON")
        

    elif hour>=12 and hour<16:
        speak("Good Afternoon sir i'm ULTRON how may i help you sir")
        

    elif hour>=16 and hour<20:
        speak("Good Evening Sir i'm ULTRON i hope you have taken your evening snack how may i help you sir  ")
        

    elif hour>=20 and hour<24:
        speak("Sir this your sleeping time what happened and how may i help you")
        

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

    print(query)

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

   elif "Google" in  query:
        speak("ok sir opening google")
        speak("here is your google enjoy ")
        webbrowser.open("www.Google.com")

   elif "Microsoft edge" in  query:
        speak("ok sir opening microsoft edge ")
        speak("here is your microsoft edge enjoy ")
        subprocess.Popen(["MicrosoftEdge.exe"])

     


   elif "Tushar Sharma" in query:
        speak("Tushar   Sharma   is my creator  he  created  me on 23 of February 2023 he is my father and my god i can do anything for him  ")
        print("Tushar   Sharma   is my creator  he  created  me on 23 of February 2023 he is my father and my god i can do anything for him ")

        
   elif "time" in query:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak("The current time is")
        speak(current_time)

   elif "thank you" and "thank" in query:
        speak ("that's my duty sir anything else")
     
   elif "open PPT" and "ppt" in query:
        open("PowerPoint")
        speak("there is your microsoft power point")
        

   elif "MS Word" in query:
        open("Word")
        speak("there is your microsoft word")

   elif "WhatsApp" in query:
        open("whatsapp")
        speak("there is your whatsapp sir enjoy your chat")

   elif "weather" in query:
        open("Weather")
        speak("This is the current weather")

   elif "raining" in query:
        speak("sir i think you should take an umbrella or you can go with the cab") 
        speak("i have mention some cab Apps for you You can ride OLA or Uber")

   elif "I look stylish" in query:
        speak("Sir there is no doubt that you are stylish")
        speak("The way you make me no one can make me like this")

   elif "I get a girl" in query:
        speak("Sir i think that you have fall in love with her that's why you saying this ")

   elif "hey Ultron" in query:
        speak("what happen sir")

   elif "files" in query:
        open("File Explorer")
        speak("there are your files Sir")

   elif "Anupama" in query:
        speak("Anupama eek number kee bahan ki laudi ha uski maa ki chuut")

   elif "I want proper answer" in query:
        speak("Sir if you want proper answer you can try on google here is the link")
        open("Google Chrome")

   elif "Will i get married or not" in query:
      speak("This will depend on you sir or the destiny of your fate")

   elif "I want to play a game" in query:
      subprocess.run(["python","game.py"])
   
   elif "Puran Chand Sharma" in query:
        speak("He is good and gentleman, he is the father of my creator Mr.Tushar Sharma ,he can do anything he give lots of money and desi ghee ka ghewar to agra people ")
      
   elif "Anju Sharma" in query:
        speak("She is the mother of my creator Mr.Tushar Sharma,She is very good generious lady ")
     
   elif "Yeh Rishta Kya Kehlata Hai" in query:
        speak("ye serial ek number ka maadarchod serial ha kabhi end nahi hota is serial ki maa ki chuuut serial")
   













     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
   elif "stop" in query:
      speak("good bye sir have a great day")
      break

    


        

     