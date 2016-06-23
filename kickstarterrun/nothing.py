


from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import etree

import threading
import Queue
import datetime
import generateallurl
import opt
urls = generateallurl.seekurl(1,54,200)

def searchwebsite(urls):
    urls_clean_list = list(set(urls))
    #file = open("category.txt",'a')
    for i in xrange(0,len(urls_clean_list)):
        #file.write(urls_clean_list[i]+'\n')
        return urls_clean_list



print searchwebsite(urls)

print 'ok'
