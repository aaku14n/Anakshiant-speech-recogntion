import re
import pyttsx
import urllib2
from BeautifulSoup import BeautifulSoup
import speech_recognition as sr
r = sr.Recognizer()
engine = pyttsx.init()
engine.setProperty('rate', 200)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_10.0' )
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
        
def information_key(key):
    key= key.title()
    ke=re.sub(r"\s+","_",key)
    url="https://en.wikipedia.org/wiki/"
    url = url+ke
    try:
        data = urllib2.urlopen(url).read()[5000:27000]
        data = data.decode("utf-8")
        soup = BeautifulSoup(data)
        a=soup.findAll('p')
    except Exception as ex:
        a='xdfd'
        print(ex)
    if a!='xdfd':
        print("yes")
        engine.say("Sir i Found something about "+key)
        engine.runAndWait()
        engine.say("Sir may i continue or leave it") 
        engine.runAndWait()
        input_user = ignore_or_cont()
        if "nope" in input_user or "no" in input_user  or "leave it" in input_user or "not yet" in input_user:
            engine.say("Ok sir thank you") 
            engine.runAndWait()
        elif "yes" in input_user or "keep it up" in input_user or "go forword" in input_user or "continue" in input_user or "yeah" in input_user:
            for tag in a:
                print (tag.getText(separator=u' '))
                engine.say(tag.getText(separator=u' '))
                engine.runAndWait()
##    else:
##        data = urllib2.urlopen(url).read()[:10000]
##        data = data.decode("utf-8")
##        soup = BeautifulSoup(data)
##        a=soup.findAll('ul')
##        for tag in a.findAll('li'):
##            print(tag.a["href"]+"***"+tag.a.string)
        #data = urllib2.urlopen(url).read()
        #data = data.decode("utf-8")
        #soup = BeautifulSoup(data)
        #a=soup.findAll('div',{"class":"searchdidyoumean"})
        #print ("error")

    
