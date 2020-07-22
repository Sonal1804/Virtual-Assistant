import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

dict1={'sonal':'sonalmisal@gmail.com', 'misal':'misalsayali19@gmail.com','sayali':'sayalimisal16@gmail.com'}

with open("Password.txt") as f:
    password=f.read()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        print("Good Morning !")
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        print("Good Afternoon !")
        speak("Good Afternoon !")
    else:
        print("Good Evening !")
        speak("Good Evening !")
    speak("Hey I am ZIRA Dear, Please tell me how may I help you")


def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in') #Using google for voice recognition.
        print(f'User said : {query}\n')      #User query will be printed
    except Exception as e:
        print("Say that again Please...")  #It will be printed in case of improper voice
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sonalmisal1804@gmail.com',password)
    server.sendmail('sonalmisal1804@gmail.com',to,content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #without this command, speech will not be audible to us


if __name__ == '__main__':
    wishme()
    while True:
        query=takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query=query.replace('wikipedia',"")
                result=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                speak(result)
            except Exception as e:
                speak("Sorry Dear,Information is not available")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir='F:\Music'
            songs=os.listdir(music_dir)
            choose=random.choice(songs)
            os.startfile(os.path.join(music_dir,choose))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f'Dear, the time is {strTime}')

        elif 'open pycharm' in query:
            codePath=r'C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.3\bin\pycharm64.exe'
            os.startfile(codePath)

        elif 'email' in query:
            try:
                for items in dict1:
                    if items in query:
                        speak("What should I say?")
                        content = takeCommand()
                        to =dict1[items]
                        sendEmail(to, content)
                        speak("Email has been sent!")
            except Exception as e:
                speak("Sorry Dear, I am not able to send this Email")

        elif 'news' in query:
            url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=04a4c808777140359356e18c32cafea2')
            abc = requests.get(url)
            response = abc.json()
            for i in range(0,5):
                speak(response['articles'][i]['title'])

        elif 'thank you' in query:
            speak("Take Care Dear")
            sys.exit()





