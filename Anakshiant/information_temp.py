import re
import pyttsx
import urllib2
from BeautifulSoup import BeautifulSoup
import speech_recognition as sr
r = sr.Recognizer()
engine = pyttsx.init()
engine.setProperty('rate', 200)
def ignore_or_cont():
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Tell me!")
            aud = r.listen(source)
        try:
            input_user = r.recognize_google(aud)
        except sr.UnknownValueError:
            input_user = "jjjj"
            engine.say("Sorry sir i am not getting you") 
            engine.runAndWait()
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            input_user = "jjjj"
            print("Sorry sir; {0}".format(e))
        print (input_user)
        if "nope" in input_user or "no" in input_user  or "leave it" in input_user or "not yet" in input_user or "yes" in input_user or "keep it up" in input_user or "go forword" in input_user or "continue" in input_user or "yeah" in input_user:
            return input_user
            break
def find_main_func(data):
    print("main")
    data = data.decode("utf-8")
    soup = BeautifulSoup(data)
    a=soup.findAll('p')
    engine.say("Sir i Found something about "+key)
    engine.runAndWait()
    engine.say("Sir may i continue or leave it") 
    engine.runAndWait()
def find_sub_func(data):
    print ("sub")
    a=soup.findAll("ul")
    b=a[0]
    print (a[0])
    engine.say("Sir i Found something about "+key)
    engine.runAndWait()
    engine.say("Sir may i continue or leave it") 
    engine.runAndWait()
    for tag in a[13].findAll('li'):
        print(tag.a["href"]+"***"+tag.a.string)
def did_not_found():
    print ("not")
def information_key(key):
    key= key.title()
    ke=re.sub(r"\s+","_",key)
    url="https://en.wikipedia.org/wiki/"
    url = url+ke
    print (url)
    try:
        data = urllib2.urlopen(url).read()[10000:27000]
        print (data)
        find_main_func(data)
    except:
        try:
            data = urllib2.urlopen(url).read()
            find_sub_func(data)
        except:
            data ="akarsh"
            did_not_found()
    
    
    
    
    

    #input_user = ignore_or_cont()
    if "nope" in input_user or "no" in input_user  or "leave it" in input_user or "not yet" in input_user:
        engine.say("Ok sir thank you") 
        engine.runAndWait()
    elif "yes" in input_user or "keep it up" in input_user or "go forword" in input_user or "continue" in input_user or "yeah" in input_user:
        for tag in a:
            print(tag.text.strip(""))
            engine.say(tag.text.strip(" "))
            engine.runAndWait()
##    else:
##
##        
##        data = data.decode("utf-8")
##        soup = BeautifulSoup(data)
##        a=soup.findAll('ul')
##        for tag in a.findAll('li'):
##            print(tag.a["href"]+"***"+tag.a.string)
##        #data = urllib2.urlopen(url).read()
        #data = data.decode("utf-8")
        #soup = BeautifulSoup(data)
        #a=soup.findAll('div',{"class":"searchdidyoumean"})
        #print ("error")
information_key("lalganj")
    
