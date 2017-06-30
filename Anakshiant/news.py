import re
import pyttsx
import urllib2
from BeautifulSoup import BeautifulSoup
engine = pyttsx.init()
engine.setProperty('rate', 200)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_10.0' )
def news_head_lines():
    url="http://timesofindia.indiatimes.com"
    data = urllib2.urlopen(url).read()
    data = data.decode("utf-8")
    soup = BeautifulSoup(data)
    a=soup.findAll('ul',{"class":"list8"})
    top_story="<html><body>"+str(a[0])+"</body></html>"
    so = BeautifulSoup(top_story)
    body_tag= so.body.ul
    count = 0
    temp= []
    for i in body_tag:
        if count%2 != 0:
            temp.append(i)
        count = count+1
    head_line= []
    for i in temp:
        news="<html><body>"+str(i)+"</body></html>"
        s = BeautifulSoup(news)
        head_line.append(s.body.li.a.string)
        print (s.body.li.a.string)
        engine.say(s.body.li.a.string)
        engine.runAndWait()
    
