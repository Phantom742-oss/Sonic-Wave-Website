'''import speech_recognition as sr
import gTTs
import pyglet
import datetime

r = sr.Recognizer()

def listen_for_command():
  with sr.Microphone() as source:
    print("Listening for command...")
    audio = r.listen(source)
  try:
    command = r.recognize_google(audio)
    print("You said: " + command)
    return command
  except sr.UnknownValueError:
    print("Sorry, I didn't understand that.")

def process_command(command):
  if "what is your name" in command:
    response = "My name is D.U.D.E."
  elif "what time is it" in command:
    current_time = datetime.datetime.now().time()
    response = "The current time is " + str(current_time)
  elif "thank you" in command:
    response = "You're welcome!"
  else:
    response = "I'm sorry, I didn't understand that command. Could you please try again?"
  return response

def speak(text):
  tts = gTTs(text)'''





'''import speech_recognition as sr
import subprocess

def listen_for_command():
    # Set up the recognizer
    r = sr.Recognizer()
    mic = sr.Microphone()

    # Listen for the command
    with mic as source:
        print("Listening...")
        audio = r.listen(source)

    # Recognize the command
    transcribed_command = r.recognize_google(audio)
    print("Command: " + transcribed_command)

    return transcribed_command

def perform_task(command):
    if "open music app" in command:
        subprocess.call(["open", "spotify"])
    elif "play my playlist" in command:
        subprocess.call(["play", "tension free"])

if __name__ == "__main__":
    command = listen_for_command()
    perform_task(command)'''


































































'''import pyttsx3
engine = pyttsx3.init()
                                          #engine.say("Hello, world i'm DuDE assistant of Mr Tushar Sharma")
                                          #engine.runAndWait()
rate= engine.getProperty("rate")
print(rate)
engine.setProperty("rate",170)
volume= engine.getProperty("volume")
print(format(volume))
engine.setProperty("volume",5)
voices=engine.getProperty("voices")
print("Male Voice :{0}".format(voices[0].id))
print("Female Voice :{0}".format(voices[1].id))
engine.setProperty("voice",voices[1].id)
engine.say("hello i'm LISSA i'm personal assistant of maker Mr. Tushar Sharma ")
engine.runAndWait()'''





















'''import speech_recognition as sr
import pyttsx3
import datetime

r = sr.Recognizer()
engine = pyttsx3.init()

def listen_for_command():
  with sr.Microphone() as source:
    print("Listening for command...")
    audio = r.listen(source)
  try:
    command = r.recognize_google(audio)
    print("You said: " + command)
    return command
  except sr.UnknownValueError:
    print("Sorry, I didn't understand that.")

def process_command(command):
  if "what is your name" in command:
    response = "My name is D.U.D.E."
  elif "what time is it" or "what is the time" in command:
    current_time = datetime.datetime.now().time()
    response = "The current time is " + str(current_time)
  elif "thank you" in command:
    response = "You're welcome!"
  else:
    response = "I'm sorry, I didn't understand that command. Could you please try again?"
  return response

def speak(text):
  engine.say(text)
  engine.runAndWait()

current_hour = datetime.datetime.now().hour
if current_hour < 12:
  greeting = "Good morning"
else:
  greeting = "Good evening"
speak(greeting)

while True:
  command = listen_for_command()
  response = process_command(command)
  speak(response)'''



