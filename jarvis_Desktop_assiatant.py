import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import webbrowser
import os
import sys
import wikipedia
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def whishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")
    else:
        speak("Good Evening!")
    speak("I am Robo Sir. please tell me how may i help you")

def TakeCommand():
    '''
    it takes a microfone input from user and return string output
    '''
    r = sr.Recognizer()
    print('Listerning...')
    with sr.Microphone() as sources:
        r.pause_threshold = 1
        audio = r.listen(sources)
    
    try:
        print("recognizing....")
        qurey = r.recognize_google(audio,language='en-in')
        print(f"User said : {qurey}\n")
    except Exception as e:
        # print("hiiiiiii")
        print(e)
        print("say that again please .....")
        return "None"
    return qurey
    # r = sr.Recognizer()
    # print("Listerning....")
    # with sr.Microphone() as sources:
    #     r.pause_threshold = 1
    #     audio = r.listen(sources)
    # try:
    #     print("Recognizing....")
    #     query = r.recognize_google(audio,language="en-in")
    #     print(f"User said : {query}\n")
    # except Exception as e:
    #     print(e)
    #     print("say that again please....")
    #     return "None"
    # return query




if __name__ == "__main__":

    whishMe()
    # TakeCommand()
    while True:
        query = TakeCommand().lower()

        if 'open google' in query:
            webbrowser.open("https://www.google.co.in/")
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google translate' in query:
            webbrowser.open("https://www.google.com/search?q=google+translate&oq=g&aqs=chrome.0.69i59l2j69i57j69i59j69i60l4.1301j0j7&sourceid=chrome&ie=UTF-8")
        
        elif 'wikipedia' in query:
            speak("wikipedia searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        
        elif 'play music' in query:
            music_dir = 'D:\\Music'
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,song[random.randint(0,len(song))]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)
        
        elif 'VLC' in query:
            vlcPath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcPath)
        
        elif 'open code' in query:
            codePath = "C:\\Users\\hingu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'exit' in query:
            sys.exit()
        
        

