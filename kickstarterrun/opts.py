
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import etree
from twisted.enterprise import adbapi
#import MySQLdb
#import MySQLdb.cursors




#someurl = 'https://www.kickstarter.com/projects/neliobarros/nixin-typeface?ref=discover_potd'
#someurl = 'https://www.kickstarter.com/projects/1060627644/35000-years-in-the-making-pens-made-from-ancient-k?ref=category_featured'
def OnlyStr(s,oth=''):
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789:,'
    for c in s:
         if not c in fomart:
             s = s.replace(c,'');
             return s;


def opt(someurl):
    global item
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
            item = {}

        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            item = {}
    else:
        for line in the_page1:
            if 'data'  in line:
                words = line.split('" ')
                for word in words:
                    if 'data class="Project' in word:
                        project_ID_str = word.split('Project')[1]
        project_ID = ''.join(project_ID_str)
        data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')
        data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')
        data_pool_url = ''.join(str(x) for x in data_pool_url)
        data_pool_url_websites = urllib2.urlopen(data_pool_url).read()
        data_pool_url_websites = ''.join(str(x) for x in data_pool_url_websites)
        a = data_pool_url_websites#.split(',')
        #print a
        name =[]
        #transfor list to dictionary
        b = OnlyStr(a).strip('project:')
        for i in range(0,len(b.split(','))):
            name.append(b.split(',')[i].split(':'))
        dics = dict(name)
        state = dics['state']
        item[ 'Project ID']= project_ID
        item[ 'projetc_state' ]= state
    return item






def fullurl(someurl):
    global wasd
    root_url = 'https://www.kickstarter.com'
    try:
        
        content = urllib2.urlopen(someurl).read()
        sel= etree.HTML(content)

    except URLError as e:
        if hasattr(e, 'reason'):
            #print 'We failed to reach a server.'
            #print 'Reason: ', e.reason
            wasd =[]
        elif hasattr(e, 'code'):
            #print 'The server couldn\'t fulfill the request.'
            #print 'Error code: ', e.code
            wasd=[]
    else:

        x = sel.xpath('//*[@id="projects_list"]/div[*]/li[*]/div/div[2]/*/a/@href')
        #x2 = sel.xpath('//*[@id="projects_list"]/div[*]/li[*]/div/div[2]/div/a/@href')
        x = list(set(x))
        if x != []:
            wasd=[]
            for i in range(0,len(x)):
                wasd.append(root_url +x[i])
    return wasd
