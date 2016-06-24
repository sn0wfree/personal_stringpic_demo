

from urllib2 import Request, urlopen, URLError
import time
import urllib2
import requests
from lxml import etree




someurl = 'https://www.kickstarter.com/projects/elijahkavana/action-deck-to-spark-your-journey?ref=category_newest'


response = Request(someurl)
content = urllib2.urlopen(someurl).read()
sel= etree.HTML(content)
##this is for some data without tab.
req = urlopen(response)
the_page1 = req.readlines()
print  response,content,sel,req,the_page1
