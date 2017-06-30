from datetime import datetime
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 150)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_10.0' )
class jar_alarm():
    def speak_alarm(self,speech):
        engine.say(speech)
        engine.runAndWait()
    def __init__(self):
        minute= datetime.now().minute
        minute= str(minute).zfill(2)
        hour= datetime.now().hour
        hour= str(hour).zfill(2)
        cur_tim=hour+minute
        cur_tim=int(cur_tim)
        f = open('jar_alarm.txt', 'r')
        for line in f:
            #print (line[:4])
            #print (int(line[:4])-3)
            min_tm= int(line[:4])-3
            max_tm= int(line[:4])+3
            if min_tm<cur_tim<max_tm:
                print ("wake up")
                self.speak_alarm(line[5:])


