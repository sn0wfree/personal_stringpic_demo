

from urllib2 import Request, urlopen, URLError
import time
import urllib2
import requests
from lxml import etree
start = time.time()
someurl='https://www.kickstarter.com/projects/windowfarms/learn-to-grow-and-share-with-new-windowfarms'


suburl_words =['description', 'updates','comments']
for word in suburl_words:
    locals()['someurl_%s'% word] = someurl + '/'+word
    locals()['response_%s'% word]= Request(locals()['someurl_%s'% word])
    locals()['content_%s'% word] = urllib2.urlopen(locals()['someurl_%s'% word]).read()
    locals()['sel_%s'% word]= etree.HTML(locals()['content_%s'% word])
    locals()['req_%s'% word] = urlopen(locals()['response_%s'% word])
    locals()['the_page1_%s'% word] = locals()['req_%s'% word].readlines()
    print locals()['sel_%s'% word]
print sel_description,sel_description.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/a[1]/text()')

end = time.time()
print end-start
