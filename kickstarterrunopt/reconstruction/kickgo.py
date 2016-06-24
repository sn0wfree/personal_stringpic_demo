import funcforkick
import kickspider
#import downloadurl
import threading
import Queue
import datetime
import time
import sys




def main(url,core):
    a = len(url)
    for j in xrange(core):
        t = ThreadClass(queue)
        t.setDaemon(True)
        t.start()
    for i in range(0,a):
        queue.put(url[i])
    queue.join()




#construct opt index dic for list
##read original index
#f = 'index.csv'
#f_items = 'data.csv'
#f_rewards = 'rewards.csv'
#index =csv_reader(f)
queue = Queue.Queue()
class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while 1:
            target = self.queue.get()
            print 'begin collecting data'
            (total_item,total_rewards)=funcforkick.basedprocess(target)


            #x = discorurl(target)
            #file = open('allurlforkicktest.txt','a')
            #writeafile(x,file)
            #time.sleep(1/10)
            self.queue.task_done()
start = time.time()
count = 0
#global index
global total_item
global total_rewards
print 'begin to creat index file'

file_values ='index_value.txt'
file_keys = 'index_keys.txt'


index = funcforkick.index_read(file_keys,file_values)
print 'begin to scrap'
#total_item_lines = open ('data.txt','r').readlines()
#total_rewards_lines= open ('rewards.txt','r').readlines()
#index = {}
total_item=[]
total_rewards=[]

#read projetc urls
print 'begin reading urls file'
file_unclear = open('allurlforkicktest.txt','r').readlines()
print 'reading list completed'
file =list(set(file_unclear))
print len(file)
lenfile200 = len(file)/200
lenfile = len(file)
print 'reading urls file completed'
print 'begin to collecting data'
#for i in xrange(1,lenfile200+1):
#    if lenfile200 >1:
#        if i < lenfile200 :
#            for j in xrange((i-1)*200,i*200):
#                locals()['urls%s' %i].append(file[j])
#        else:
#            for j in xrange ((lenfile200-1)*200,lenfile):
#                locals()['urls%s' % lenfile200].append(file[j])
#    else:
#        for j in xrange(0,lenfile):
#            urls1.append(file[j])
#main(file ,3)
count = 0
for i in xrange(0,len(file)):
    someurl=file[i]
    (item,rewards,ID,state)= kickspider.kickgowebscraper(someurl)
    total_item.append(item)
    total_rewards.append(rewards)
    time.sleep(1)
    sys.stdout.write("\rthis spider has already collected %d project" % count)
    count = count + 1
    sys.stdout.flush()



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


#total_item.close()
#total_rewards.close()

#lentotal_item = len(total_item)
#lentotal_rewards = len(total_rewards)
#for i in xrange(0,lentotal_item):
#    total_item.write(total_item[i]+'\n')
#    total_rewards.write(total_rewards[i]+'\n')





#csv_writer(index,f,w)

funcforkick.index_write(index,file_keys,file_values)
#csv_writer(total_item,f_items,a)
#csv_writer(total_rewards,f_rewards,a)
end = time.time()
print end-start
