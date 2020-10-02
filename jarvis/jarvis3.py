import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# function that will help computer to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# function to recognise your voice
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
        print(e)
        print("Say that again please...")
        return "None"
    return query


def write(name, content):
    with open(name, "w") as f:
        f.write(content)


speak("Enter the name of the file: ")
name = takeCommand().lower()
speak("Enter what you want to write: ")
content = takeCommand().lower()

write(name, content)