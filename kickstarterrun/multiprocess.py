import threading
import Queue
import datetime
import generateallurl
import opt
import time
import sys

def progress_test():
  bar_length=20
  for percent in xrange(0, 100):
    hashes = '#' * int(percent/100.0 * bar_length)
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent: [%s] %d%%"%(hashes + spaces, percent))
    sys.stdout.flush()
    time.sleep(1)
progress_test()


#urls = open("category.txt",'r').readlines()



queue = Queue.Queue()


#for i in xrange(0,len(urls)):
#    file2.write(urls[i]+'\n')
def writeafile(x,y):
    clean_list = list(set(x))
    if clean_list != []:
        lenallurl_clean_list = len(clean_list)
        for i in xrange(0, lenallurl_clean_list):
            y.write(clean_list[i]+'\n')
    return clean_list

class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while 1:
            target = self.queue.get()
            x = generateallurl.discorurl(target)
            url1 = writeafile(x,file)
            allurl=[]
            if  url1 != [] :
                lenurl1 = len(url1)
                for j in xrange(0,lenurl1):
                    allurl.append(url1)

            self.queue.task_done()


def main():

    for j in xrange(4):
        t = ThreadClass(queue)
        t.setDaemon(True)
        t.start()
        for url in urls:
            queue.put(url)
    queue.join()


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
