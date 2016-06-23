import threading
import Queue
import datetime

import opt
import time
import sys
#1,2,3,4,5,6,8,9,13,14,15,17,18,19,20,21,22,23,24,25,26,27,29,32,33,34,36,39,38,40,41,42,43,4,45,46,47,48,49,50,51,53
start = time.time()



n=1
x=54
y=1
l=0
k=1
j=97
url = []
#global wasd

alla =[]
good =[]
empty =[]
for i in xrange(n, x):
    q = 'https://www.kickstarter.com/discover/advanced?category_id='+ str(i) + '&pledged='+ str(k) + '&goal='+ str(l) + '&sort=newest&seed=2409590&page=' + str(j+1)
    if  opt.fullurl(q) == []:
        print '%s is empty' % i
        empty.append(str(i))
    else:
        print '%s is good' % i
        good.append(str(i))
        #q.append(str('https://www.kickstarter.com/discover/advanced?category_id='+ str(i) + '&pledged='+ str(k) + '&goal='+ str(l) + '&sort=newest&seed=2409590&page=' + str(j+1)))
        alla.append(q)
        #q = 'https://www.kickstarter.com/discover/advanced?category_id='+ str(i) + '&pledged='+ str(k) + '&goal='+ str(l) + '&sort=newest&seed=2409590&page=' + str(j+1)
                #print type(q)
#category_urls = open ('category1.txt','r').readlines()
#print len(category_urls)
#allurl =   open ('allurlforkick.txt','r').readlines()
#print len(allurl)                 #if i ==1-6,8,9 53and

print len(alla)
print 'when k= %s,l=%s,j = %s' %(k ,l, j)

print 'good :',good           #break
end = time.time()
print end-start
                #else:
#()if not i in (7, 10 ,11, 12, 16 ,28, 30 ,31 ,35)

#k,l=2;j=50
#good =['1', '7', '9', '10', '11', '12', '14', '16', '18', '28', '30', '34']
#k,l=2;j=40 (1, 7, 9, 10, 11, 12, 14, 16, 18, 28 ,30,34)
#good =['1', '7', '9', '10', '11', '12', '14', '16', '18', '28', '30', '31', '32', '34', '35']
#k,l=2;j=45
#good =['1', '7', '9', '10', '11', '12', '14', '16', '18', '28', '30', '34', '35']

#(1, 7, 9, 10, 11, 12, 14, 16, 18, 28 ,30,34)
#7,    10 ,11, 12,     16 ,28, 30 ,      31 ,35




#print allurl_clean_list





#file = open("all.txt",'a')

    #print i
    #allurl = generateallurl.discorurl(url[i])
    #file.write(allurl[j]+'\n')

        #print "%s says Hello World at time: %s \n" % (self.getName(), now)
#for i in xrange(4):
#    t = ThreadClass()
#    t.start()


#time.sleep(0)
