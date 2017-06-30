import speech_recognition as sr
import aiml
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 150)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_10.0' )
# Record Audio
r = sr.Recognizer()
#sr.energy_threshold = 300
def chat():
    # Create the kernel and learn AIML files
    question = "XFIND Jarvis"
    kernel = aiml.Kernel()
 #   kernel.learn("alice.aiml")
#    kernel.learn("alice/ai.aiml")
    kernel.learn("alice/xfind.aiml")
#    kernel.learn("alice/date.aiml")
#    kernel.learn("alice/atomic.aiml")

 #   kernel.learn("alice/bot.aiml")
#    kernel.learn("alice/that.aiml")
    kernel.learn("alice/stories.aiml")

    kernel.learn("alice/stack.aiml")
    kernel.learn("alice/sports.aiml")
    kernel.learn("alice/sex.aiml")
    kernel.learn("alice/science.aiml")
 #   kernel.learn("alice/religion.aiml")
 #   kernel.learn("alice/salutations.aiml")
 #   kernel.learn("alice/reductions-update.aiml")
 #   kernel.learn("alice/reduction4.safe.aiml")
    #kernel.learn("alice/update_mccormick.aiml")
#    kernel.learn("alice/update1.aiml")
 #   kernel.learn("alice/wallace.aiml")
    kernel.learn("alice/reduction3.safe.aiml")
    kernel.learn("alice/reduction2.safe.aiml")
  #  kernel.learn("alice/reduction1.safe.aiml")
    kernel.learn("alice/reduction0.safe.aiml")
 #   kernel.learn("alice/pyschology.aiml")
 #   #kernel.learn("alice/primitive-math.aiml")
    kernel.learn("alice/primeminister.aiml")
    kernel.learn("alice/pickup.aiml")
    kernel.learn("alice/numbers.aiml")
    kernel.learn("alice/mp5.aiml")
#    kernel.learn("alice/mp4.aiml")
    kernel.learn("alice/mp3.aiml")
    kernel.learn("alice/mp2.aiml")
#    kernel.learn("alice/mp1.aiml")
    kernel.learn("alice/mp0.aiml")
    kernel.learn("alice/iu.aiml")
    kernel.learn("alice/loebner10.aiml")
    kernel.learn("alice/iu.aiml")
    kernel.learn("alice/humor.aiml")
 #   kernel.learn("alice/imponderables.aiml")
 #   kernel.learn("alice/inquiry.aiml")
    kernel.learn("alice/interjection.aiml")
    engine.say(kernel.respond(question))
    engine.runAndWait()

    # Press CTRL-C to break this loop
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("You:")
            audio = r.listen(source)
        try:
            question = r.recognize_google(audio)
            if "stop chat" in question or "stop" in question:
                engine.say("ok,nice to talk to you sir")
                engine.runAndWait()
                break
            question = question.upper()
            print (question)
            res= kernel.respond(question)
            print (res)
            engine.say(res) 
            engine.runAndWait()

            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



