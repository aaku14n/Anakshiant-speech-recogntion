from gtts import gTTS
from tempfile import TemporaryFile
tts = gTTS(text='Hello', lang='en')
f = TemporaryFile()
tts.write_to_fp(f)
if tts.write_to_fp(f) == True:
    print ("yes")
f.close()
