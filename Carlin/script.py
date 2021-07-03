import speech_recognition as sr
import os


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        try:
            r.pause_threshold = 1
            audio = r.listen(source)
        except Exception as e:
            print(e)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Your command is {query} ")

    except Exception as e:
        print(e)

    if "hey Carlin" in query or "wake up" in query:
        os.startfile('tt.py')

    return query.lower()


while True:
    listen()

