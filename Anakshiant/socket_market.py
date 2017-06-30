import re
import urllib2
import pyttsx
engine = pyttsx.init()
def stock_market(path):
    url ="https://www.google.com/finance?q="
    key=path
    url = url + key #concatation of the strings
    data = urllib2.urlopen(url).read()
    data = data.decode("utf-8")
    m = re.search('<meta itemprop="price"',data)
    start = m.end() + 18
    end = start + 16
    newString = data[start:end]
    me = re.search("/",newString)
    end = me.start() - 2
    engine.say(" Sir,the stock market of the " + key + " is " + newString[0:end])
    engine.runAndWait()
    


