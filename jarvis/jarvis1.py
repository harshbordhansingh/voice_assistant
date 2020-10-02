import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
isTrue = False


''' 
this function will help jarvis to speak 
'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


''' 
this function will help jarvis to wish us 
'''
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0  and hour < 12:
        speak("Good morning sir, i will be very greatfull to help you.")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir, i will be very greatfull to help you.")
    else:
        speak("Good evening sir, i will be very greatfull to help you.")

    speak("How may i help you?")


def takeCommand():
    # it will recognise our voice and help jarvis to do our work
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
        print(e)
        print("Say that again please...")
        return "None"
    return query


def googling(ask):
    speak("Searching Google...")
    webbrowser.open("https://google.com/?#q=" + ask)


def write(name, content):
    with open(name, "w") as f:
        f.write(content)

    
def writing():
    speak("Please tell me the name of the file: ")
    name = takeCommand().lower()
    speak("What you want to write: ")
    content = takeCommand().lower()

    write(name, content)


def wiki(question):
    speak("Wait a second sir, searching wikipedia...")
    question = question.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak("Sir, according to wikipedia")
    speak(results)


''' 
this is the main function
'''
if __name__ == "__main__":
    listen = takeCommand().lower()
    if 'hello jarvis' in listen:
        wishMe()
        while True:
            query = takeCommand().lower()

            # logic for executing task based on query
            if 'quit' in query:
                speak("Thanks for your time sir, have a nice day, me jarvis signing off.")
                break
            
            elif 'wikipedia' in query:
                wiki(query)
                isTrue == True

            elif 'how are you' in query:
                speak("I am fine sir")
                isTrue == True
            
            elif 'open youtube' in query:
                speak("Opening you tube...")
                webbrowser.open("youtube.com")
                isTrue == True

            elif 'open stack overflow' in query:
                speak("Opening stack overflow")
                webbrowser.open("stackoverflow.com")
                isTrue == True

            elif 'open google' in query:
                speak("Opening google")
                webbrowser.open("google.com")
                isTrue == True

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                isTrue == True

            elif 'open code' in query:
                code_path = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)
                isTrue == True

            elif 'write a file' in query:
                writing()
                isTrue == True

            elif isTrue == False:
                googling(query)

    else:
        speak("Sorry sir, you are not allowed to acess this")