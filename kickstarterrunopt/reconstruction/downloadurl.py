import funcforkick
#import kickspider
import threading
import Queue
import datetime
import time
import sys


start = time.time()
count = 0
global count
##generate category url
#file = open('categoryurl1.txt', 'w')
#category_urls = funcforkick.generatecategoryurl(file)
#file.close()
##using already generate url to do next
categoryurl = open('categoryurl.txt','r').readlines()
categoryurl_clean = list(set(categoryurl))

#print len(categoryurl_clean)
#print categoryurl[1]
#print categoryurl_clean[1]

funcforkick.downloadforurl(categoryurl_clean,12)
print '\nDownload and save project_url tasks have completed'








#project_urls = pool.map(funcforkick.daufcurl,urls)
#pool.close()
#pool.join()
#print type(project_urls)
#print project_urls
##save project urls
#file_for_project_urls = open('allprojecturls.txt','w')
#funcforkick.writeafile(project_urls,file_for_project_urls,0)






#print '\nok'

#begin download data for each project






















#i = int(input("Please enter an integer(1-54):"))
#urls = generateallurl.seekurl(i,i+1,200)#oringal(1,54,200)11-54
#file = open ('url%s.text' % i , 'a')
#file.close()

#import kick
#urls = open ('category2.text','r').readlines()

#file = open('allurlforkicktest1.text','w')
#(file,urls) = firstset(x)
#queue = Queue.Queue()
#file = open ('category2.text' , 'w')
#urls = generateallurl.seekurl(1,54,200)#oringal(1,54,200)11-54
#file.write(urls[i]+'\n')
#file = open('url.text'.'r')

#for i in xrange(0, len(urls)):
#    file.write(urls[i]+'\n')
#class ThreadClass(threading.Thread):
#    def __init__(self, queue):
#        threading.Thread.__init__(self)
#        self.queue = queue
#    def run(self):
#        while 1:
#            target = self.queue.get()
#            item = kick.webscraper(target)

#            self.queue.task_done()


#def main():

#    for j in xrange(4):
#        t = ThreadClass(queue)
#        t.setDaemon(True)
#        t.start()
#        for url in urls:
#            queue.put(url)
#    queue.join()
#main()
end = time.time()
print end-start
