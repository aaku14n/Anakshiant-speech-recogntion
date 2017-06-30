import speech_recognition as sr
import time
t1=time.time()
import subprocess
import os
#import pyglet
import pyttsx
import datetime
from difflib import SequenceMatcher
import socket_market
import news
import information
import ai_chat
import re
from datetime import date
from  jar_alarm import jar_alarm
import webbrowser
from Tkinter import *
from PIL import Image, ImageTk
engine = pyttsx.init()
engine.setProperty('rate', 200)
#sr.adjust_for_ambient_noise(source, duration = 1)
#engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_10.0' )
# Record Audio



r = sr.Recognizer()
#sr.energy_threshold = 2000
def wake_up():
    engine.say("ok sir")
    engine.runAndWait()
    wake_status = 1
    while wake_status:
        jar_alarm()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            path = r.recognize_google(audio)
            if "wake up" in path:
                wake_status = 0
                engine.say("Yes sir")
                engine.runAndWait()
        except sr.UnknownValueError:
            pass
        
    
#project gui

top=Tk()

def helloCall(strs):
    a=Label(top,text=strs)
    a.place(x=0,y=0)




#function for the predicting of the path in the speech of the user
def find_all_directory(self,path,folder):
    print(path)
    a=next(os.walk(path))[0]
    print(a)
    b= []
    global x
    for i in a:
        b.append(SequenceMatcher(None, i, folder).ratio())
    max_probability = max(b)
    x = b.index(max(b))
    max_probability = max_probability*100
    if max_probability >=80:
        print (a[x])
        return x,a[x]
    else:
        return 0

  
#class for the connection with akarshb
class con_with_me(object):
    
    def hi_aaku_connection(self,path):
        now = datetime.datetime.now()
        
        if 0<=now.hour<12:
            say_to ="Good morning"
        elif 11<now.hour<17:
            say_to ="Good After noon"
        elif 16<now.hour:
            say_to = "Good Evening"
        
        engine.say("Hello sir"+ str(say_to))
        engine.runAndWait()
        #pyglet.media.load("sounds/hello.mp3",streaming= False).play()
        
    def how_calss_connection(self):
        engine.say("I am fine sir,and how are you")
        engine.runAndWait()
    def hi_aaku_name(self):
        engine.say("Sir ,I am Jarbis,and i am  program")
        engine.runAndWait()
    def hi_aaku_time(self):
        now = datetime.datetime.now()
        engine.say("Sir ,It's time "+str(now.hour) +":"+str(now.minute))
        engine.runAndWait()
    def hi_aaku_date(self):
        now = datetime.datetime.now()
        engine.say("Sir ,It's date "+date(day=now.day,month=now.month,year=now.year).strftime('%A %d %B %Y'))
        engine.runAndWait()
    def hi_aaku_thank(self):
        engine.say("your wellcome Sir")
        engine.runAndWait()

        
#class for opening content
class open_class(object):
    
    #def set_var(self):
    second_last_path=""
    last_path=""
    global current_path 
    def open_computer(self):
        print ("tes")
        subprocess.Popen(r'explorer /select,"c:\"')
    def open_disk(self,path):
        if os.path.isdir(path+':/') == True:
            os.startfile(path+':/')
            print(os.startfile(path+':/'))
            op = open_class()
            op.second_last_path = "none"
            op.last_path = "computer"
            op.current_path = path+':'
        else:
            print("not found")
##            sound = pyglet.media.load("aaku.wav",streaming= False)
##            sound.play()
##            time.sleep(3)
            get_voice_input()
    def go_back(self):
        op = open_class()
        op.current_path = op.last_path
        op.last_path = op.second_last_path
        op.second_last_path = "none"
        if os.path.isdir(op.current_path) == True:
            os.startfile(op.current_path)
        else:
            sound = pyglet.media.load("aaku.wav",streaming= False)
            sound.play()
            time.sleep(3)
            get_voice_input()
    def open_folder(self,path):
        op = open_class()
        print path
        op.current_path = op.last_path
        path=find_all_directory('',op.current_path+"/",path)[1]
        temp_path = op.current_path+"/"+path
        os.startfile(temp_path)
        
        op.second_last_path = op.last_path
        op.last_path = op.current_path
        op.current_path = temp_path
    def open_chrome(self):
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

#Get User input
def get_voice_input():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        t2=time.time()
        print(t2-t1)
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    try:
       
        # instead of `r.recognize_google(audio)`
        path = r.recognize_google(audio)
        #helloCall(path)
        length=len(path)
        print("You said: " + path)
        
        if path == "computer" or path == "my computer":
            op = open_class()
            op.open_computer()
        elif path == "take rest":
            wake_up()
        elif path[:10] == "local disc" or path[:10] == "new volume":
            op = open_class()
            op.open_disk(path[length-1:length])
        elif path == "go back":
            op = open_class()
            op.go_back()
        elif "hi Jarvis" in path or "hello" in path:
            con=con_with_me()
            con.hi_aaku_connection(path)
        elif "how are you" in path or "tum kaise ho" in path:
            con=con_with_me()
            con.how_calss_connection()
        elif "news" in path:
            news.news_head_lines()
        elif "stock market" in path:
            socket_market.stock_market(path[16:])
        elif "what is your name" in path or 'who are you' in path:
            con=con_with_me()
            con.hi_aaku_name()
        elif "current time" in path:
            con=con_with_me()
            con.hi_aaku_time()
        elif ("ok" or "Yeah" or "ya") == path:
            pass
        elif "thank you Jarvis" in path:
            con=con_with_me()
            con.hi_aaku_thank()
        elif "start chat" in path:
            ai_chat.chat()
        elif "current date" in path:
            con=con_with_me()
            con.hi_aaku_date()
        elif "do you know" in path:
            m=re.search("do you know",path)
            end_of_world=m.end()+1
            path = path[end_of_world:]
            information.information_key(path)
        elif "open folder" in path:
            m=re.search("open folder",path)
            end_of_world=m.end()+1
            path = path[end_of_world:]
            op = open_class()
            op.open_folder(path)
        elif "open Chrome" in path or "open Google Chrome" in path:
            op = open_class()
            op.open_chrome()
        else:
            engine.say("Sorry ,sir i am not getting you")
            engine.runAndWait()
    except sr.UnknownValueError:
        print("ANAKSHIANT Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from ANAKSHIANT Speech Recognition service; {0}".format(e))

image = Image.open('a.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(top, image = photo_image)
label.pack()
##
##def task():
##   # jar_alarm()
##    get_voice_input()
##    top.after(2000,task)
##
##top.after(2000,task)
##top.mainloop()
#loop rolling
while 1:
    jar_alarm()
    get_voice_input()
    #top.mainloop()
#top.mainloop()
    


    
