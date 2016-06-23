
from urllib2 import Request, urlopen, URLError

import urllib2
import requests
from lxml import etree
import pickle
import time

import opt
import opts

#find all category links
def seekurl(n,x,y):
    url = []
    for i in xrange(n, x):#category
        for l in xrange(0,4):
            for k in xrange(0, 4):
                #pledged max 4
                for j in xrange(0, y):#pages
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



#find all url for each category link
def discorurl(y):
    x = opt.fullurl(y)
    someurl = []
    if x != []:
        someurl = x
    return someurl

#file2 = open("urltest.txt",'r').readlines()
#print type(file2)
#print file2
#allurl= list(set(file2))
#print allurl
#f = open('allurl.txt','w')
#for i in xrange(0,len(allurl)-1):
#    file.write(url[i]+'\n')
#file = open('url.txt', 'r' ).readlines()
#fi = open ('usefull_url','w')
#print file[1]
#for i in xrange(0,8):
#    if opt.fullurl(file[i]) != []:
#        a.append(opt.fullurl(file[i]))
#print a
#    if a != []:
#        print 1
#    else:
#        print 0
        #someurl.append(a)
#print someurl



#for i in xrange(400,1000):
#    usefull_url = opt.fullurl(url[i])
#    if usefull_url <> []:
#        someurl.append(usefull_url)

#file = open("someurl.txt",'w')
#for i in xrange(0,len(someurl)):

#    f.write (someurl[i]+'\n')



#pickle.dump(''.join(someurl), f)
#response = Request(someurl)
#ontent = urllib2.urlopen(someurl).read()
#sel= etree.HTML(content)
##this is for some data without tab.
#req = urlopen(response)
#the_page1 = req.readlines()
#for i in xrange(0 len(url)):
#    item={}
#    item = webscraper(url[i])
#print 'ok'
