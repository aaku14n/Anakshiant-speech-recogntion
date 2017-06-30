import speech_recognition as sr
import time
import pyttsx

from threading import *
r = sr.Recognizer()
class jar_timer():
    global st
    def input_for_timer(self):
        
        path=''
        while path!='Stop':
            with sr.Microphone() as source:
                print"say"
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                path = r.recognize_google(audio)
                print path
                for thread in enumerate():
                    print "h"
                    if thread.isAlive():
                        print"xfv"
                        try:
                            thread.clear()
                        except:
                            print(str(thread.getName()) + ' could not be terminated')
                self.timer_func.Event.set()
                if path=='stop':
                    
                    st= False
                    self.timer_func.set()
            except sr.UnknownValueError:
                pass
            
    def timer_func(self,path):
        i=0
        print path
        while path:
            i=i+1
            time.sleep(1)
            print i

    def __init__(self):
        st = True
        Thread(target= self.input_for_timer).start()
        Thread(target= self.timer_func(st)).start()        
jar_timer()
