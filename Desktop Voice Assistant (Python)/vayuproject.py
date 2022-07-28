# DESKTOP VOICE ASSISTANT - VAYU
# BY GROUP NUMBER 25

import ntpath
import operator
import random
import sys
import time
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon") 
    else:
        speak("Good Evening")
    
    speak("Hello I am Vaayyu What can i do For you ?")
            
                
                
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'Vaayyu' in query:
            print("yes sir")
            speak("yes sir")
            
        elif "who are you" in query:
            print("My Name is Vaayyu")
            speak("My name is Vaayyu")
            
            print("I can do Everything My creator programmed me to do")
            speak("I can do Everything My creator programmed me to do") 
        
        elif "who created you" in query:
            print("I was created by group number 25")
            speak("I was created by group number 25")
        
        elif "what is" in query:
            speak('Searching wikipedia..')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "who is" in query:
            speak('Searching wikipedia..')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'just open google' in query:
            webbrowser.open('google.com')
        
        elif 'open google' in query: #7
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)
        
        elif 'search on google' in query:
            s=query[16:]
            query = query.replace("search on google", "")
            webbrowser.open(f"www.google.com/search?q="+s)
        
        
        elif 'search on youtube' in query:
            s=query[18:]
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query="+s)
        
        elif 'open MS edge' in query:
            npath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" 
            os.startfile(npath)
               
        elif 'close MS edge' in query:
            os.system("taskkill /f /im msedge.exe")            
        
        # elif 'open chrome' in query:
        #     npath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        #     os.startfile(npath)
         
        
        elif 'open notepad' in query:
            npath = "C:\Windows\System32\\notepad.exe" 
            os.startfile(npath)
        
        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")
            
        elif 'open winrar' in query:
            npath = "C:\Program Files\WinRAR\WinRAR.exe" 
            os.startfile(npath)                
        
        elif 'close winrar' in query:
            os.system("taskkill /f /im winrar.exe")    
          
                
        elif 'close vlc' in query:
            os.system("taskkill /f /im vlc.exe") 
            
        elif "open command prompt" in query: #17
            os.system("start cmd")
        
        elif "close command prompt" in query: #18
            os.system("taskkill /f /im cmd.exe")    
            
        elif 'play music' in query: #19
            music_dir = 'D:\Musics'
            songs = os.listdir(music_dir)    
            os.startfile(os.path.join(music_dir, random.choice(songs)))    
            
        elif 'play iron man movie' in query: #20
            npath = ("D:\ironman.mp4")    
            os.startfile(npath)
            
        elif 'close movie' in query: #21
            os.system("taskkill /f /im vlc.exe")

        elif 'close music' in query: #22
            os.system("taskkill /f /im vlc.exe") 
        
        elif 'tell current time' in query: #23
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")    
            
        elif "shut down the system" in query: #24
            os.system("shutdown /s /t 5")

        elif "restart the system" in query: #25
            os.system("shutdown /r /t 5")

        elif "lock the system" in query: #26
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "hibernate the system" in query: #27 
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    
            
        elif "go to sleep" in query: #29
            speak(' alright then, I am switching off')
            sys.exit()    
            
        elif "take screenshot" in query: #30
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()  
            img.save(f"{name}.png")  
            speak("screenshot saved")

        elif "calculate" in query: #31
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listning...")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                }[op]
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))    
            
        elif "what is my ip address" in query: #32
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org/').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")
        
        elif "volume up" in query: #33
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            
        elif "volume down" in query: #34
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        
        if 'open chrome' in query:
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe') 


        elif 'maximize window' in query:            
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
            
        elif 'google search' in query:
            query= query.replace("google search", "")
            pyautogui.hotkey('alt','d')
            pyautogui.write(f"{query}",0.1)
            pyautogui.press('enter')
            
        elif 'youtube search' in query:
            query= query.replace("youtube search", "")
            pyautogui.hotkey('alt','d')        
            time.sleep(1)
            pyautogui.press('tab') 
            pyautogui.press('tab') 
            pyautogui.press('tab') 
            pyautogui.press('tab') 
            time.sleep(1)
            pyautogui.write(f"{query}",0.1)
            pyautogui.press('enter')            
        
        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')
            
            
        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
            
        elif 'minimise  window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
        
          
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')
        
        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')
        
        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        
        elif 'next tab' in query:
            pyautogui.hotkey('ctrl',  'tab')
                   
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl',  'w')           
            
        elif 'close window' in query:
            pyautogui.hotkey('ctrl',  'shift', 'w')    
        
        
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
            
                      
    # THANK YOU   