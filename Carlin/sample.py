import webbrowser
import winsound
from covid import Covid
from time import*
import speech_recognition as sr
import pyttsx3
import pyautogui
import screen_brightness_control as sb
import psutil
import cv2
from Covid19India import CovidIndia
import os
import pywhatkit
import webbrowser as web
from pytube import *
from pyautogui import *
import pyperclip
import wolframalpha
from keyboard import press_and_release
import speedtest
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import pyjokes
import randfacts
import requests
import datetime
import music
import Face_recognition
from tkinter import *


engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
client = wolframalpha.Client("")#Enter your wolframalpha Api key by creating an account


def speak(audio):
    print(f"{audio}")
    engine.say(audio)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"Your command is {query} ")
        except:
            return ""

    return query.lower()


MASTER = "Geethika"


def wishme():
    press('esc')
    speak("Verification Successful...")
    speak("Running Carlin program...")
    hr = int(datetime.datetime.now().hour)
    if 0 <= hr < 12:
        speak("Good Morning " + MASTER)
    elif 12 <= hr < 16:
        speak("Good Afternoon " + MASTER)
    elif hr >= 16:
        speak("Good Evening " + MASTER)
    speak("How May I Help You...")


def exe():
    while True:

        query = listen()
        if "need a break" in query or "sleep" in query:
            speak("Ok mam, I'm going to sleep mode")
            speak("If you need any help, just say hey carlin or wake up")
            exit()
            break

        elif "volume" in query:
            vol(query)

        elif "brightness" in query:
            brightness(query)

        elif "battery" in query:
            battery()

        elif "photo" in query or "pic" in query or "picture" in query:
            photo()

        elif "shutdown" in query:
            shut()

        elif "restart" in query:
            res()

        elif "video" in query:
            video()

        elif "search on youtube" in query:
            query = query.replace("search", "")
            query = query.replace("on youtube", "")
            youtube(query)

        elif "download this video" in query:
            ytd()

        elif "google search" in query:
            query = query.replace("google search", "")
            google(query)

        elif "what time is it" in query or "what is the time" in query:
            p=strftime("%H")
            r=strftime("%M")
            speak("Current time is "+p+" hours "+r+" minutes")

        elif "day" in query:
            now = datetime.datetime.today().strftime("%A")
            speak("Today is "+now)

        elif "date" in query:
            g=datetime.datetime.today().strftime("%d")
            e = datetime.datetime.today().strftime("%m")
            t = datetime.datetime.today().strftime("%Y")
            speak("Today's date is "+g+" "+e+" "+t)

        elif "locate" in query or "navigate" in query or "where is" in query:
            query = query.replace("locate ","")
            query = query.replace("navigate ", "")
            query = query.replace("where is","")
            googlemaps(query)


        elif 'temperature' in query:
            term = str(query)
            term = term.replace("ok ", "")
            term = term.replace("carlin ", "")
            term = term.replace("in ", "")
            term = term.replace("what is the ", "")
            term = term.replace("temperature ", "")
            tempquery = str(term)
            if "outside" in tempquery:
                var = "Temperature in Delhi"
                a = wolfram(var)
                speak(f"{var} is {a} .")
            else:
                var1 = "Temperature in " + tempquery
                ans = wolfram(var1)
                speak(f"{var1} is {ans} .")

        elif 'notepad' in query:
            notepad()

        elif 'dismiss' in query:
            query = query.replace("dismiss" , "")
            closenotepad()

        elif "chrome mode" in query:
            chromemode()

        elif "speed" in query:
            speedTest(query)

        elif "remember this" in query:
            remember(query)

        elif "remind me" in query:
            rem()

        elif "education mode" in query:
            edu()

        elif "youtube mode" in query or "youtube mod" in query:
            yta()

        elif "whatsapp" in query:
            whatsapp()

        elif "instagram" in query:
            insta()

        elif "news" in query:
            news()

        elif 'joke' in query:
            jokes()

        elif 'fact' in query:
            facts()

        elif "d drive" in query:
            os.startfile("D:\\")

        elif "e drive" in query:
            os.startfile("E:\\")

        elif "c drive" in query:
            os.startfile("C:\\")

        elif "song" in query or "music" in query:
            music.music()

        elif "screenshot" in query:
            screenshot()

        elif "current location" in query:
            cl()

        elif "alarm" in query:
            speak("please tell me the time to set alarm")
            tt=listen()
            tt=tt.replace("set alarm to","")
            tt=tt.replace(".","")
            tt=tt.upper()
            alarm(tt)

        elif "corona cases" in query:
            speak("Please specify the Country name...")
            uu=listen()
            worldcorona(uu)


def worldcorona(country):
    obj = Covid(source="worldometers")
    co = obj.get_status_by_country_name(country)
    speak(f"Total number cases in {country}: {co['total_cases']}")
    speak(f"New cases in {country}: {co['new_cases']}")
    speak(f"Number of deaths in {country}: {co['deaths']}")
    speak(f"Recovered cases in {country}: {co['recovered']}")
    speak(f"Active cases in {country}: {co['active']}")



def vol(query):
    if "volume up" in query:
        pyautogui.press("volumeup")
        speak("Your volume has been increased")
    elif "volume down" in query:
        pyautogui.press("volumedown")
        speak("Your volume has been decreased")
    elif "mute volume" in query:
        pyautogui.press("volumemute")
        speak("Your volume has been muted")


def brightness(query):
    if "brightness to hai" in query:
        sb.set_brightness(100)
        speak("Your brightness has been set to high")
    elif "brightness to low" in query:
        sb.set_brightness('-100')
        speak("Your brightness has been set to low")
    elif "brightness to medium" in query:
        sb.set_brightness(50)
        speak("Your brightness has been set to medium")


def battery():
    battery = psutil.sensors_battery()
    speak(f"Your battery percent is {battery.percent}")
    if battery.power_plugged:
        speak("Your PC is plugged in")
    else:
        speak("Your PC is unplugged")
    convert(battery.secsleft)


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    speak(f"Your pc will function upto {hour} hour {minutes} minutes")


def photo():
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    for i in range(3):
        return_value, image = camera.read()
        cv2.imwrite('photos//opencv' + str(i) + '.png', image)
    speak("Your picture has been saved to photos in carlin folder")
    del camera

def video():
    vid_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    vid_cod = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("videos//cam_video.mp4", vid_cod, 20.0, (640, 480))
    speak("Your video has started")
    speak("press, 'g', to stop your video")
    speak("Your video will be saved to videos in carlin folder")
    while True:
        ret, frame = vid_capture.read()
        cv2.imshow("My cam video", frame)
        output.write(frame)
        if cv2.waitKey(1) & 0XFF == ord('g'):
            break
    vid_capture.release()
    output.release()
    cv2.destroyAllWindows()


def shut():
    os.system("shutdown /s /t 1")


def res():
    os.system("shutdown /r /t 1")


def youtube(query):
    result = "https://www.youtube.com/results?search_query=" + query
    web.open(result)
    speak("This is what i found for your search .")
    pywhatkit.playonyt(query)
    speak("This may also help you.")


def ytd():
    sleep(5)
    click(x=942, y=59)
    # click(x=1250, y=75)
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'c')
    link = pyperclip.paste()
    Link = str(link)
    speak("Your video is downloaded into the carlin folder")
    YouTube(Link).streams.first().download('E:\\Python Projects\\Carlin\\videos\\')


def google(query):
    speak("This is what i found for your search")
    pywhatkit.search(query)


def maps(query):
    location = query.replace("where is","")
    speak("Hold on mam, I will show you where " + location + " is.")
    web.open("https://www.google.nl/maps/place/" + location + "/&amp;")


def wolfram(query):
    api_key="85X7L5-WPL898JGK8"
    requester=wolframalpha.Client(api_key)
    requested=requester.query(query)
    try:
        answer=next(requested.results).text
        return answer
    except:
        speak("A string value is not answerable")


def notepad():
    speak("Tell me the content .")
    speak("I am ready to write .")
    writes = listen()
    time = datetime.datetime.now().strftime("%H:%M")
    filename = str(time).replace(":","-")+ "-note.txt"
    with open(filename,"w") as file:
        file.write(writes)
    path1 = "E:\\Python Projects\\Carlin\\"+str(filename)
    path2 = "E:\\Python Projects\\Carlin\\Notes\\"+str(filename)
    os.rename(path1,path2)
    os.startfile(path2)


def closenotepad():
    os.system("TASKKILL /F /im Notepad.exe")
    speak("your notepad is closed and is saved to carlin folder")


def chromemode():
    speak("Chrome mode activated")
    webbrowser.open(url='https://www.google.com')
    speak("Tell your command sir")
    while True:
        try:
            com = listen()
            print(com)
            com = com.lower()
            if "incognito tab" in com:
                press_and_release('ctrl + shift + n')
            elif "new tab" in com:
                press_and_release('ctrl + t')
            elif "new window" in com:
                press_and_release('ctrl + n')
            elif "switch tab" in com:
                press_and_release('ctrl + tab')
            elif "download" in com:
                press_and_release('ctrl + j')
            elif "history" in com:
                press_and_release('ctrl + h')
            elif "close tab" in com:
                press_and_release('ctrl + w')
            elif "reopen closed tab" in com:
                press_and_release('ctrl + shift + t')
            elif "reload" in com:
                press_and_release('ctrl + r')
            elif "back" in com:
                press_and_release('alt + left')
            elif "next" in com:
                press_and_release('alt + right')
            elif "close window" in com:
                press_and_release('alt + f4')
            elif "bookmark" in com:
                press_and_release('ctrl + shift + o')
            elif "clear browsing data" in com:
                press_and_release('ctrl + shift + delete')
            elif "search" in com:
                speak("what to search ?")
                com = listen()
                google(com)
            elif "source code" in com:
                press_and_release('ctrl + u')
            elif "add to bookmark" in com:
                press_and_release('ctrl + d')
            elif "scroll down" in com:
                press_and_release('space')
            elif "scroll up" in com:
                press_and_release('shift + space')
            elif "exit chrome mode" in com:
                press_and_release('alt + f4')
                speak("Chrome mode exited")
                break
        except:
            continue


def speedTest(query):
    speak("Checking Your internet speed....")
    speed=speedtest.Speedtest()
    downloading=speed.download()
    cd=int(downloading/800000)
    uploading=speed.upload()
    cu=int(uploading/800000)
    if 'uploading' in query:
        speak(f"Uploading speed is {cu} mbps")
    elif 'downloading' in query:
        speak(f"Downloading speed is {cd} mbps")
    else:
        speak(f"Your internet Uploading speed is {cu} mbps and Downloading speed is {cd} mbps")


def remember(rmsg):
    rmsg = rmsg.replace("remember this","")
    rmsg = rmsg.replace("carlin ","")
    remember = open('data.txt', 'w+')
    remember.write(rmsg)
    remember.close()
    speak("ok, i remember this. ask me to remind you whenever you want .")


def rem():
    reme=open("data.txt","r")
    speak("You told me to remind you this message :" + reme.read())

def insta():
    web.open('https://www.instagram.com')


def news():
    apikey = "4ad432c899d345f6b946ed73db668cbd"
    mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4ad432c899d345f6b946ed73db668cbd"
    news = requests.get(mainurl).json()
    article = news['articles']
    newsarticle = []
    for arti in article:
        newsarticle.append(arti['title'])

    for i in range(10):
        speak(newsarticle[i])
        engine.runAndWait()


def jokes():
    speak("Here's a joke!")
    speak(pyjokes.get_joke())


def facts():
    speak(randfacts.getFact())



def edu():
    speak("Education mode activated!!")
    while True:
        sleep(2)
        speak("ask your question mam..")
        abc = listen()

        if "exit education mode" in abc:
            speak("Education mode exited")
            break

        abc = abc.replace("plus","+")
        abc = abc.replace("minus", "-")
        abc = abc.replace("power", "^")
        abc = abc.replace("by", "/")
        abc = abc.replace("into", "*")
        try:
            wolfram_res = next(client.query(abc).results).text
            speak(wolfram_res)
        except:
            speak("No data available")

        engine.runAndWait()


def googlemaps(place):
    speak("Hold on mam, I will show you where " + place + " is.")
    url_place="https://www.google.com/maps/place/"+str(place)
    geolocator=Nominatim(user_agent="myGeocoder")
    location=geolocator.geocode(place,addressdetails=True)
    target_loc=location.latitude,location.longitude
    location=location.raw['address']
    target={'city':location.get('city',''), 'state':location.get('state',''), 'country' :location.get('country','')}
    current_loc=geocoder.ip('me')
    current_latlon=current_loc.latlng
    distance=str(great_circle(current_latlon,target_loc))
    distance=str(distance.split(' ',1)[0])
    distance=round(float(distance),2)
    web.open(url=url_place)
    speak(target)
    speak(f"{place} is {distance} kilometer away from your location .")


def whatsapp():
    web.open("https://web.whatsapp.com/")
    sleep(10)
    speak("Tell the contact name")
    name = listen()
    pyautogui.click(x=124, y=230)
    pyautogui.doubleClick()
    press('delete')
    pyautogui.typewrite(name)
    sleep(1)
    pyautogui.click(x=217, y=432)
    speak("What do you want to do mam")
    speak("Do you want me to send message, or call, or video call")
    task = listen()
    if "message" in task:
        pos = pyautogui.locateOnScreen("emoji.png", confidence=.6)
        # pos1 = pt.locateOnScreen("Emoji.png", confidence=.6)
        x = pos[0]
        y = pos[1]
        pyautogui.moveTo(x + 200, y + 20, duration=.5)
        pyautogui.click()
        speak("Tell your message which has to be sent")
        message = listen()
        pyautogui.typewrite(message, interval=.01)
        pyautogui.typewrite("\n", interval=.01)
        speak("Message sent!")

    elif "video" in task:
        pos = pyautogui.locateOnScreen("video.png", confidence=.6)
        x = pos[0]
        y = pos[1]
        pyautogui.moveTo(x, y , duration=.5)
        pyautogui.click()

    elif "call" in task:
        pos = pyautogui.locateOnScreen("call.png", confidence=.9)
        x = pos[0]
        y = pos[1]
        pyautogui.moveTo(x, y, duration=.5)
        pyautogui.click()


def yta():
    speak("Youtube mode activated")
    webbrowser.open(url='https://www.youtube.com/')
    speak("Tell me your command")
    while True:
        com = listen()
        print(com)
        com = com.lower()
        if "pause" in com:
            press_and_release('space bar')
        elif "play" in com:
            press_and_release('space bar')
        elif "full screen" in com:
            press_and_release('f')
        elif "theatre mode" in com:
            press_and_release('t')
        elif "fast forward" in com:
            press_and_release('l')
        elif "back forward" in com:
            press_and_release('j')
        elif "increase speed" in com:
            press('>')
        elif "decrease speed" in com:
            press('<')
        elif "reload" in com:
            press_and_release('ctrl + r')
        elif "previous" in com:
            press_and_release('shift + p')
        elif "next" in com:
            press_and_release('shift + n')
        elif "close youtube" in com:
            press_and_release('alt + f4')
        elif "download" in com:
            ytd()
        elif "history" in com:
            web.open("https://www.youtube.com/feed/history")
        elif "search" in com:
            speak("what do you want to search for ?")
            query = listen()
            result = "https://www.youtube.com/results?search_query=" + query
            web.open(result)
            speak("This is what i found for your search .")
            speak("This may help you.")
        elif "open youtube" in com:
            webbrowser.open(url='https://www.youtube.com/')
        elif "exit youtube mode" in com:
            press_and_release('alt + f4')
            speak("youtube mode exited")
            break

def alarm(timing):
    altime=str(datetime.datetime.now().strptime(timing,"%I:%M %p"))
    altime=altime[11:-3]
    h=altime[:2]
    h=int(h)
    m=altime[3:5]
    m=int(m)
    speak(f"Done mam, alarm set at {timing}")
    while True:

        if h==datetime.datetime.now().hour:
            if m==datetime.datetime.now().minute:
                print("Alarm is running")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif m<datetime.datetime.now().minute :
                break

def screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'Screenshots\\screenshot.png')
    speak("Screenshot is taken and saved to photos in carlin folder .")

def cl():
    r=requests.get('https://get.geojs.io./')
    ipreq=requests.get('https://get.geojs.io/v1/ip.json')
    ipadd=ipreq.json()['ip']

    url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
    georeq=requests.get(url)
    geodata=georeq.json()

    speak("City : " + geodata['city'])
    speak("Region : "+ geodata['region'])
    speak("Country : "+ geodata['country'])
    speak("Current Timezone : "+ geodata['timezone'])
    speak("Latitude : "+ geodata['latitude'])
    speak("Longitude : "+ geodata['longitude'])

def ert():
    r = requests.get('https://get.geojs.io./')
    ipreq = requests.get('https://get.geojs.io/v1/ip.json')
    ipadd = ipreq.json()['ip']

    url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
    georeq = requests.get(url)
    geodata = georeq.json()
    return geodata['country']

def security():
    speak("Recognizing and Verifying face...Please wait...")

    if Face_recognition.facerec():
        wishme()
        exe()
    else:
        try:
            def check():
                if pwd.get() == "geethu":
                    speak("Access granted!")
                    win.destroy()
                    wishme()
                    exe()
                else:
                    speak("Incorrect password... Terminating Program...")
                    win.destroy()

            speak("Face recognition failed")
            speak("Enter correct password to get access")
            win = Tk()
            win.title('Verification')
            win.geometry("800x400")
            win.config(background="black")
            pwd = StringVar()
            msg = Label(text="Enter Password :", font=('Comic Sans MS', 16, "bold"), background="black", fg='White')
            msg.place(x=100, y=100)
            entry = Entry(win, textvariable=pwd, font=15, bd='3')
            entry.place(x=400, y=110)
            set = Button(text="Submit", command=check, font=('Comic Sans MS', 13), bg='#567', fg='White')
            set.place(x=330, y=200)
            win.mainloop()
        except:
            print()












