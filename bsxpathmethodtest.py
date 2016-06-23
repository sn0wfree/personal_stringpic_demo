
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import etree
#from twisted.enterprise import adbapi
#import MySQLdb
#import MySQLdb.cursors

def retype(x):
    x_new = ''.join(x)
    return x_new


names = locals()
someurl = 'https://www.kickstarter.com/discover/advanced?category_id=0&amp;pledged=0&amp;goal=1&amp;raised=1&amp;sort=newest&amp;seed=2409590&amp;page=1'

root_url = 'https://www.kickstarter.com'

try:
      response = Request(someurl)

      content = urllib2.urlopen(someurl).read()

      sel= etree.HTML(content)
      ##this is for some data without tab.
      req = urlopen(response)
      the_page1 = req.readlines()
except URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason

    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:
    x = sel.xpath('//*[@id="projects_list"]/div[1]/li[*]/div/div[2]/h6/a/@href')
    #print x
    fullurl=['']*len(x)
    for i in range(0,len(x)):
        fullurl[i]=root_url +x[i]
    #print fullurl
    #return fullurl
#print usefullurl(1)
