# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

#Initiating Speech Engine
engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice','voice[1].id')

#Converting Text to Speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Welcome Message
def greetMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

#Command Function 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go Ahead, I'm Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio,language = 'en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry, I can't hear that")
            return "None"
        return statement

print("Loading Your Personal Assistant Mike")
speak("Loading Your Personal Assistant Mike")
greetMe()

#Main Function
if __name__=='__main__':
    while True:
        speak("Hi, how can I help you ?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Until we meet again, Take care')
            print('Until we meet again, Take care')
            break
        
        if 'wikipedia' in statement:
            speak('Searching Wikipedia....')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences = 3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Opening Youtube")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Opening Google Mail")
            time.sleep(5)

        elif 'open twitter' in statement:
            webbrowser.open_new_tab("https://twitter.com/login")
            speak("Opening Twitter")
            time.sleep(5)
        
        elif 'open amazon' in statement:
            webbrowser.open_new_tab("https://www.amazon.in/")
            speak("Opening Amazon")
            time.sleep(5)

        elif 'open netflix' in statement:
            webbrowser.open_new_tab("https://www.netflix.com/")
            speak("Opening Netflix")
            time.sleep(5)

        elif 'open yahoo' in statement:
            webbrowser.open_new_tab("https://in.yahoo.com/")
            speak("Opening Yahoo")
            time.sleep(5)
        
        elif 'open whatsapp' in statement:
            webbrowser.open_new_tab("https://www.whatsapp.com/")
            speak("Opening Whatsapp")
            time.sleep(5)
        
        elif 'open reddit' in statement:
            webbrowser.open_new_tab("https://www.reddit.com/")
            speak("Opening Reddit")
            time.sleep(5)

        elif 'open linkedin' in statement:
            webbrowser.open_new_tab("https://www.linkedin.com/signup")
            speak("Opening Linkeedin")
            time.sleep(5)

        elif 'open github' in statement:
            webbrowser.open_new_tab("https://github.com/")
            speak("Opening Github")
            time.sleep(5)
        
        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what's the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"] != "404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" Unable to find the city ")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")   
        
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Mike your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was developed by Prashanth")
            print("I was developed by Prashanth")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="54H9GA-27Y2U8444T"
            client = wolframalpha.Client('54H9GA-27Y2U8444T')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)


        


         
