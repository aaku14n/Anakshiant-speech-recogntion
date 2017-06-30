import speech_recognition as sr
import time
t1=time.time()
import subprocess
import os
import pyglet
import pyttsx
import datetime
from difflib import SequenceMatcher
import socket_market
import news
import information
import ai_chat
engine = pyttsx.init()
engine.setProperty('rate', 200)
# Record Audio
r = sr.Recognizer()
#sr.energy_threshold = 300

#function for the predicting of the path in the speech of the user
def find_all_directory(self,path,folder):
    a=next(os.walk(path))[1]
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
        if 0<now.hour<12:
            say_to ="Good morning"
        elif 12<now.hour<17:
            say_to ="Good After noon"
        elif 17<now.hour:
            say_to = "Good Evening"
        
        engine.say("Hello sir"+say_to)
        engine.runAndWait()
        #pyglet.media.load("sounds/hello.mp3",streaming= False).play()
        
    def how_calss_connection(self):
        engine.say("I am fine sir,and how are you")
        engine.runAndWait()
    def hi_aaku_name(self):
        engine.say("Sir ,I am Jarbis, created by aakarsh yadav")
        engine.runAndWait()
    def hi_aaku_time(self):
        now = datetime.datetime.now()
        engine.say("Sir ,It's time "+str(now.hour) +":"+str(now.minute))
        engine.runAndWait()
    def hi_aaku_thank(self):
        engine.say("your wellcome ,Sir")
        engine.runAndWait()

        
#class for opening content
class open_class(object):
    
    def set_var(self):
        second_last_path
        last_path
        current_path = "ada"
    def open_computer(self):
        print ("tes")
        subprocess.Popen(r'explorer /select,"c:\"')
    def open_disk(self,path):
        if os.path.isdir(path+':/') == True:
            os.startfile(path+':/')
            print(os.startfile(path+':/'))
            open_class.set_var.second_last_path = "none"
            open_class.set_var.last_path = "computer"
            open_class.set_var.current_path = path+':'
        else:
            print("not found")
            sound = pyglet.media.load("aaku.wav",streaming= False)
            sound.play()
            time.sleep(3)
            get_voice_input()
    def go_back(self):
        
        open_class.set_var.current_path = open_class.set_var.last_path
        open_class.set_var.last_path = open_class.set_var.second_last_path
        open_class.set_var.second_last_path = "none"
        if os.path.isdir(open_class.set_var.current_path) == True:
            os.startfile(open_class.set_var.current_path)
        else:
            sound = pyglet.media.load("aaku.wav",streaming= False)
            sound.play()
            time.sleep(3)
            get_voice_input()
    def open_folder(self,path):
        print (open_class.set_var.current_path,path)
        zx= find_all_directory(open_class.set_var.current_path+"/",path)
        if zx != '0':
            path=find_all_directory(open_class.set_var.current_path+"/",path)[1]
            temp_path = open_class.set_var.current_path+"/"+path
            os.startfile(temp_path)
            open_class.set_var.second_last_path = open_class.set_var.last_path
            open_class.set_var.last_path = open_class.set_var.current_path
            open_class.set_var.current_path = temp_path

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
        length=len(path)
        print("You said: " + path)
        
        if path == "computer" or path == "my computer":
            op = open_class()
            op.open_computer()
        elif path[:10] == "local disc" or path[:10] == "new volume":
            op = open_class()
            op.open_disk(path[length-1:length])
        elif path == "go back":
            op = open_class()
            op.go_back()
        elif "hi" in path or "hello" in path:
            con=con_with_me()
            con.hi_aaku_connection(path)
        elif "how are you" in path or "tum kaise ho" in path:
            con=con_with_me()
            con.how_calss_connection()
        elif "news" in path:
            news.news_head_lines()
        elif "stock market" in path:
            socket_market.stock_market(path[16:])
        elif "what is your name" in path:
            con=con_with_me()
            con.hi_aaku_name()
        elif "current time" in path:
            con=con_with_me()
            con.hi_aaku_time()
        elif ("ok" or "Yeah" or "ya") == path:
            pass
        elif "thank you" in path:
            con=con_with_me()
            con.hi_aaku_thank()
        elif "start chat" in path:
            ai_chat.chat()
        else:
            information.information_key(path)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#loop rolling
while 1:
    get_voice_input()
    
