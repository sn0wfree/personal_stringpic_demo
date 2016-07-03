from urllib2 import Request, urlopen, URLError
import time
import urllib2
import requests
from lxml import etree

#from PIL import Image
import pytesseract
from PIL import Image

def read_a_file(file):
    with open(file,'r') as f:
        f_collected=f.readlines()
    return f_collected
def write_a_file(file,item):
    with open(file,'w') as f:
        lenitem=len(item)
        for i in xrange(0,lenitem):
            f.write(item[i])

def webscraper_png(someurl):
    #root_url = 'https://www.kickstarter.com'
    try:
          req=requests.get(someurl)
          response = urllib2.urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason

        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code

    else:
        img_cont = response.read()




#reading a urlfiel
x='/Users/sn0wfree/Dropbox/BitTorrentSync/kickstarterscrapy/ocrforkicktraq/data/allurlforkicktest.txt'
url=read_a_file(x)
urls=list(set(url))
#print len(urls)
#print urls[23].split('https://www.kickstarter.com')[1]
kicktraq='http://www.kicktraq.com'
if '?ref=category_newest' in urls[23].split('https://www.kickstarter.com')[1]:
    a=urls[23].split('?ref=category_newest')[0]
    print a

    kicktraqurl=kicktraq+a.split('https://www.kickstarter.com')[1]
    kicktraqurl_dailypledges=''.join(kicktraqurl.split())+'/dailypledges.png'

print kicktraqurl
print kicktraqurl_dailypledges

image_file = 'dailypledges-5.png'
im = Image.open(image_file)

print type(im)
print im
