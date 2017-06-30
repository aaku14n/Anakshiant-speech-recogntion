import speech_recognition as sr
import pyttsx
r = sr.Recognizer()
engine = pyttsx.init()
engine.setProperty('rate', 200)

def get_user_input():
    a=1
    engine.say("Sir may i continue or leave it") 
    engine.runAndWait()
    while a==1:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Tell me!")
            aud = r.listen(source)
        try:
            input_user = r.recognize_google(aud)
        except sr.UnknownValueError:
            input_user = "jjjj"
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            input_user = "jjjj"
            print("Sorry sir; {0}".format(e))
        print (input_user)
        if "nope" in input_user or "no" in input_user  or "leave it" in input_user or "not yet" in input_user:
            engine.say("okkkk Sir") 
            engine.runAndWait()
            a=0
        elif "yes" in input_user or "keep it up" in input_user or "go forword" in input_user or "continue" in input_user or "yeah" in input_user:
            break

