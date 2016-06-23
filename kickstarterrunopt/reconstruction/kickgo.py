import funcforkick
import kickspider
import downloadurl
import threading
import Queue
import datetime
import time
import sys
import csv


global index
global total_item
global total_rewards



def csv_reader(file):
    for key,val in csv.reader(open(file)):
        dict[key] = val
    return dict
def csv_writer(dict,file,w):
    csvwriter =csv.writer(open(file,"%s" %w))
    for key,val in dict.items():
        csvwriter.writerrow([key,val])
    print 'saving process completed'


def datagenerateprocess(url):
    if url != '':
        (item,rewards,id,state) = kickspider.kickgowebscraper(url)
    else:
        #print 'url is empty'
        (item,rewards,id,state) =(0,0,0,0)
    return item,rewards,id,state
#construct opt index dic for list
##read original index
f = 'index.csv'
#f_items = 'data.csv'
#f_rewards = 'rewards.csv'
index =csv_reader(f)
total_item = open ('data.txt',a).readlins()

total_rewards= open ('rewards.txt',a).readlins()
#index = {}
#total_item=[]
#total_rewards=[]


queue = Queue.Queue()
class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while 1:
            target = self.queue.get()
            (item,rewards,id,state)= datagenerateprocess(target)
            (index,exist_code) = compareindexprocess(id,state,index)
            if exist_code == 1:
                total_item_part.append(item)
                total_rewards_part.append(rewards)

            #x = discorurl(target)
            #file = open('allurlforkicktest.txt','a')
            #writeafile(x,file)
            #time.sleep(1/10)
            self.queue.task_done()

#a=1 means 'replicated projetcs'

def main(url,core):
    a = len(url)
    for j in xrange(core):
        t = ThreadClass(queue)
        t.setDaemon(True)
        t.start()
    for i in range(0,a):
        queue.put(url[i])
    queue.join()

def compareindexprocess(id,state,index):
    a=1
    if id != 0:
        if  index.has_key(id) :
            if index[id] =='live':
                index.pop(id)
                index[id]=state
                a=1
            else:
                a = 0
                #a=['replicated projetcs']
        else:
            #a=['replicated projetcs']
            a = 1
            index[id]=state
    else:
        a = 0
    return index, a





def extend_result(x,y,a,b):
    a.extend(x)
    b.extend(y)
    return a,b

#read projetc urls
print 'begin reading urls file'
file_unclear = open('allurlforkicktest.txt',r),readlines()
file =list(set(file_unclear))
lenfile200 = len(file)/200
lenfile = len(file)
print 'reading urls file completed'
print 'begin to collecting data'
for i in xrange(1,lenfile200+1):
    total_item_part=[]
    total_rewards_part=[]
    if lenfile200 >1:
        if i < lenfile200 :
            for j in xrange((i-1)*200,i*200):
                locals()['urls%s' %i].append(file[j])
        else:
            for j in xrange ((lenfile200-1)*200,lenfile):
                locals()['urls%s' % lenfile200].append(file[j])
    else:
        for j in xrange(0,lenfile):
            urls1.append(file[j])
    main(locals()['urls%s' %i],3)
    (total_item,total_rewards)= extend_result(total_item_part,total_rewards_part,total_item,total_rewards)
    timesleep(1)






























#index_file_reads = open('indexfile.txt','r').readlines()
#index_files = list(set(index_file_reads))
#index_file_read.close()
#lenindex_files = len(index_files )
#index_list =[]
#index=[]
#for i in xrange(0,lenindex_files):
#    index_list = index_files[i].split(':')
#    index.append(index_list)
#index_dict = dict(index)








total_item.close()
total_rewards.close()

lentotal_item = len(total_item)
lentotal_rewards = len(total_rewards)
for i in xrange(0,lentotal_item):
    total_item.write(total_item[i]+'\n')
    total_rewards.write(total_rewards[i]+'\n')





csv_writer(index,f,w)
#csv_writer(total_item,f_items,a)
#csv_writer(total_rewards,f_rewards,a)
