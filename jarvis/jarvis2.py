import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0  and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("How may i help you?")
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshsinghghy@gmail.com', 'your-password-here')
    server.sendmail('harshsinghghy@gmail.com', to, content)
    server.close()


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


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'email to harsh' in query:
                try:
                    speak("what should i send?")
                    content = takeCommand()
                    to = "bahubalikumar0@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry i am not able to send this email")

        elif 'quit' in query:
            break