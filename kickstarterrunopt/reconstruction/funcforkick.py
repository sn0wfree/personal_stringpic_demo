import threading
import Queue
import datetime
import time
import sys
import urllib2
import requests
from lxml import etree
import pickle
from urllib2 import Request, urlopen, URLError
import os


#generate category url
def generatecategoryurl(file):
    urls = generateallurl(1,54)
    writeafile(urls,file)

    return urls

def generateallurl(n,x):
    url = []
    for i in xrange(n, x):#category
        for l in xrange(0,4):
            for k in xrange(0, 4):
                #pledged max 4
                for j in xrange(0, 200):#pages
                    if l ==3 and k==3 and j>40:
                        break
                    else:
                        if l==2 and k==2 and j>150 and not i in (7, 11, 14):
                            break
                        else:
                            if l ==1 and k==1 and j>150 and not i in (1,7, 11, 12, 14, 17, 18, 32):
                                break
                            else:
                                if l == 0 and k ==0 and j>130 and not i in (1, 11, 14, 18):
                                    break
                                else:
                                    if l==1 and k==3 and j>45 :
                                        break
                                    else:
                                        if k == 0 and l ==3 and j> 90 :
                                            break
                                        else:
                                            if l==0 and k==3 and j>5:
                                                break
                                            else:
                                                if l ==2 and k== 3 and j>40:
                                                    break
                                                else:
                                                    if k== 1 and l==3 and j > 49:
                                                        break
                                                    else:
                                                        if  l== 3 and k==2 and j >40:
                                                            break
                                                        else:
                                                            if l==2 and k==1 and j>150 and not i in (7,11)  :
                                                                break
                                                            else:
                                                                if k==0 and l==2 and j>150 and not i in (7, 9, 10, 11, 12, 14, 16, 18):
                                                                    break

                                                                else:
                                                                    if k==2 and l==1 and j>95:
                                                                        break
                                                                    else:
                                                                        if l==0 and k==2 and j>9:
                                                                            break
                                                                        else:
                                                                            if k==1 and l==0 and j>97:
                                                                                break
                                                                            else:
                                                                                url.append('https://www.kickstarter.com/discover/advanced?category_id='+ str(i) + '&pledged='+ str(k) + '&goal='+ str(l) + '&sort=newest&seed=2409590&page=' + str(j+1))
    return url


count = 0
def writeafile(x,y):
    clean_list = list(set(x))
    global count
    hashes = '#' * int(count)
    lenallurl_clean_list = len(clean_list)
    for i in xrange(0, lenallurl_clean_list):
        if clean_list[i] != '':
            #print clean_list[i]
            y.write(clean_list[i]+'\n')
            sys.stdout.write("\rthis spider has alread written %d urls" % count)
            count = count + 1
            sys.stdout.flush()




def readfile():

    for i in xrange(1,x):
        locals()['file'+str(i)]=open('/Users/sn0wfree/Desktop/categorydata/url%s.text' %i ,'r').readlines()
        print type(locals()['file'+str(i)])
        url = url + (locals()['file'+str(i)])
        locals()['file'+str(i)].close()


    url = list(set(url))
    return url

    #print type(url)
    #print 'ok'

def collectfile(url):
    a=len(url)
    file = open('/Users/sn0wfree/Desktop/sorteddata/allurl.txt','w')
    for i in xrange(0,a):
        file.write(url[i]+'\n')
    file.close()



def progress_test():
  bar_length=20
  for percent in xrange(0, 100):
    hashes = '#' * int(percent/100.0 * bar_length)
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent: [%s] %d%%"%(hashes + spaces, percent))
    sys.stdout.flush()
    time.sleep(1)



def opt(someurl):
    #global item
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

def OnlyStr(s,oth=''):
   #s2 = s.lower();
   fomart = 'abcdefghijklmnopqrstuvwxyz0123456789:,'
   for c in s:
       if not c in fomart:
           s = s.replace(c,'');
   return s;


def daufcurl(someurl):
    wasd = []


    #global wasd
    root_url = 'https://www.kickstarter.com'
    if someurl != '':
        try:

            response = Request(someurl)
            content = urllib2.urlopen(someurl).read()
            sel= etree.HTML(content)
            req = urlopen(response)
            the_page1 = req.readlines()
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
                a=len(x)
                for i in range(0,a):
                    wasd.append(root_url +x[i])
    else:
        wasd = []
    return wasd



queue = Queue.Queue()
class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while 1:
            target = self.queue.get()
            x = discorurl(target)
            file = open('allurlforkicktest.txt','a')
            writeafile(x,file)
            #time.sleep(1/10)
            self.queue.task_done()



def main(x,y):
    a = len(x)
    for j in xrange(y):
        t = ThreadClass(queue)
        t.setDaemon(True)
        t.start()
    for i in range(0,a):
        queue.put(x[i])
    queue.join()




def downloadforurl(x,y):
    #i = int(input("Please enter an integer(1-54):"))
    #(file,urls) = firstset(x)
    #for i in range(0,len(x)):
        #uuu = discorurl(x[i])
        #global uuu
        #file = open('allurlforkicktest1.txt','a')
        #writeafile(uuu,file)
    main(x,y)

def discorurl(y):
    x = daufcurl(y)
    someurl = []
    if x != []:
        someurl = x
    return someurl
