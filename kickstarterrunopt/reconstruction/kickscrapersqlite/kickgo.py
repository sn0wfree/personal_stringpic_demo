import funcforkick
import kickspider
#import downloadurl
import threading
import Queue
import datetime
import time
import sys


import sys



start = time.time()



    # insert the data to databases





#def main(url,core):
#    a = len(url)
#    for j in xrange(core):
#        t = ThreadClass(queue)
#        t.setDaemon(True)
#        t.start()
#    for i in range(0,a):
#        queue.put(url[i])
#    queue.join()
#construct opt index dic for list
global counts
counts = 0

#queue = Queue.Queue()
#class ThreadClass(threading.Thread):
#    def __init__(self, queue):
#        threading.Thread.__init__(self)
#        self.queue = queue
#    def run(self):
#        while 1:
#            target = self.queue.get()
#            print 'begin downloading data'

#            (item,rewards,id,state)= funcforkick.datagenerateprocess(target)
#            (index,exist_code) = funcforkick.compareindexprocess(id,state,index)
            #print item,rewards

#            if exist_code == 1:
#                total_item.append(item)
#                total_rewards.append(rewards)

#            sys.stdout.write("\rthis spider has already download %d urls/project" % counts)
#            counts = counts + 1
#            sys.stdout.flush()

            #x = discorurl(target)
            #file = open('allurlforkicktest.txt','a')
            #writeafile(x,file)
            #time.sleep(1/10)
#            self.queue.task_done()


global index
global total_item
global total_rewards

print 'begin to create/read index file'
#read projetc urls
file_unclear_file = open('allurlforkicktest.txt','r')
file_unclear =file_unclear_file.readlines()
file_unclear_file.close()
index = funcforkick.index_read('index_value.txt','index_keys.txt')
total_item=[]
total_rewards=[]
#print index
#total_item_lines = open ('data.txt','r').readlines()
#total_rewards_lines= open ('rewards.txt','r').readlines()
#index = {}

#total_item= funcforkick.item_read('index.txt')

#total_rewards= funcforkick.rewards_read('rewards.txt')
#print 'reading list completed'
file =list(set(file_unclear))
#print 'reading urls file completed'
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
lenfile = len(file)

for i in xrange(0,lenfile):
    someurl=file[i]
    if someurl !='':
        (item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl)
        new_add=0
        updated=0
        repeated=0
        (exist_code,index,new_add,updated,repeated) = funcforkick.compareindexprocess(ID,state,index,new_add,updated,repeated)
        #1:new_add
        #2:updated
        #3:repeated
        if exist_code != 0:
            a=(item['creator_personal_url'],item[' creator_buildhistory_has_backed_projects_number'],item[' Goal'],item[' creator_buildhistory_has_built_projects_number'],item[' creator_bio_info_url'],item[' creator_Facebook_url'],item[' currency'],item[' duration'],item[' Project_ID'],item[' location_ID'],item[' state_changed_at'],item[' description'],item[' category'],item[' project_state'],item[' has_a_video'],item[' comments_count'],item[' updates_number'],item[' project_name'],item[' data_percent_rasied'],item[' hours_left'],item[' pledged_amount'],item[' creator_short_name'],item[' creator_friends__facebook_number'],item[' created_at'],item[' Deadline'],item[' backers_count'],item[' creator_full_name'])
            total_item.append(a)
            total_rewards.append(rewards)
            counts = counts + 1
        if len(total_item)>10:
            for x in total_item:
                funcforkick.projetcdata_txt_write(x,'item.txt')

            for y in total_rewards:
                funcforkick.projetcdata_txt_write(y,'rewards.txt')
            #reset list
            total_item=[]
            total_rewards=[]


        #conditional_insert(cursor, item)
        sys.stdout.write("\rthis spider has already read %d projects and %d new add, %d updated, %d repeated" % (counts,new_add,updated,repeated))
        sys.stdout.flush()
        #time.sleep(1)







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
#print '\n',total_item
#csv_writer(index,f,w)


print '\n the len of total_item :' , len(total_item)
funcforkick.index_write(index,'index_value.txt','index_keys.txt')
#csv_writer(total_item,f_items,a)
#csv_writer(total_rewards,f_rewards,a)

end = time.time()
print end-start
