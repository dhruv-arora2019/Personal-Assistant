import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
import wolframalpha
import json
import requests
from weather import *
#import ask

print('warming up my vocal cords!')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Warming up my voice")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('yay! I am done for the day')
            print('Goodbye, talk to you soon!')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "what's the weather like today" in statement or "Should I carry an umbrella" in statement:
            speak("Please type the city name")
            cityname=input("Enter city name please: ")
            sendweather(cityname)
            speak("here take a look")
            #speak(sendweather(current_temperature))
            #execfile(weather.py)
            

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your persoanl assistant. I am programmed to do variety of tasks, support for more tasks coming soon')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Group 5")
            print("I was built by Group 5")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

       # elif "camera" in statement or "take a photo" in statement:
          #  ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

       # elif 'ask' in statement:
          #  execfile(ask.py)
           # speak('I can answer to computational and geographical questions and what question do you want to ask now')
           # question=takeCommand()
           # app_id="R2K75H-7ELALHR35X"
           # client = wolframalpha.Client('R2K75H-7ELALHR35X')
           # res = client.query(question)
           # answer = next(res.results).text
           # speak(answer)
           # print(answer)
        elif "play on spotify" in statement:
            speak("Please type the name of the song")
            songname=input("Name of the song is: ")
            speak("currently under integration please check back later")


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)












