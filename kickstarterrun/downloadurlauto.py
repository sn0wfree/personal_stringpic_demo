import threading
import Queue
import datetime
import generateallurl
import opt
import time
import sys


#urls = open("category.txt",'r').readlines()
def firstset(x):
    a = generateallurl.seekurl(x,x+1,200)#oringal(1,54,200)11-54
    #file = open ('url%s.txt' % x , 'a')
    return (file,a)


count = 0


#for i in xrange(0,len(urls)):
#    file2.write(urls[i]+'\n')
def writeafile(x,y):
    clean_list = (x)
    global count
    hashes = '#' * int(count)
    if clean_list != []:
        lenallurl_clean_list = len(clean_list)
        for i in xrange(0, lenallurl_clean_list):
            y.write(clean_list[i]+'\n')
            sys.stdout.write("\rthis spider has alread write %d files" % count)
            count = count + 1
            sys.stdout.flush()

queue = Queue.Queue()

class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while 1:
            target = self.queue.get()
            x = generateallurl.discorurl(target)
            writeafile(x,file)

            #if  url1 != [] :
            #    lenurl1 = len(url1)
            #    for j in xrange(0,lenurl1):
            #        allurl.append(url1)

            self.queue.task_done()
urls=[]
global urls

def main():
    for j in xrange(3):
        t = ThreadClass(queue)
        t.setDaemon(True)
        t.start()
        for url in urls:
            queue.put(url)
    queue.join()


def downloadforurl(x):
    #i = int(input("Please enter an integer(1-54):"))
    urls = open ('category2.txt','r').readlines()

    global urls
    file = open('allurlforkicktest1.txt','w')
    #(file,urls) = firstset(x)

    main()
