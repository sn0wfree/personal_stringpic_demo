
import multiprocessing as mp
import sys
import funcforkick
import time
import pandas as pd
import numpy as np
import threading
import Queue
f = time.time()


global counts
counts = 0


global index


print 'begin to create/read index file'
#read projetc urls
file_unclear_file = open('data/middle60project/middle60.txt','r+')
file_unclear =file_unclear_file.readlines()
file_unclear_file.close()
new_add=0
updated=0
repeated=0
    #start = time.time()
index = funcforkick.index_read('data/middle60project/index_value.txt','data/middle60project/index_keys.txt')
total_item=[]
total_rewards_backers_distribution=[]
total_rewards_pledge_limit=[]
total_rewards_pledged_amount=[]
saving_file ='data/middle60project/project_data.csv'

rewards_backers_distribution='data/middle60project/rewards_backers_distribution.csv'
rewards_pledge_limit='data/middle60project/rewards_pledge_limit.csv'
rewards_pledged_amount='data/middle60project/rewards_pledged_amount.csv'
someurls =list(set(file_unclear))
total_item=[]
total_rewards_backers_distribution=[]
total_rewards_pledge_limit=[]
total_rewards_pledged_amount=[]

#print 'reading urls file completed'
print 'begin to collecting data'

rewards_headers=['Project_ID','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50']
item_headers = ['Project_ID','project_name','Goal','url',
                  'pledged_amount','backers_count','creator_full_name',
                  'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
                  'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']
new_add=0
updated=0
repeated=0


def collectingdate(someurl):
    start = time.time()
    global new_add
    global counts
    global index
    global rewards_headers
    global item_headers
    global total_item
    global total_rewards_backers_distribution
    global total_rewards_pledge_limit
    global total_rewards_pledged_amount
    global updated
    global repeated
    if someurl !='':
        someurl=someurl.strip()
        #global new_add
        #global updated
        #global repeated
        (exist_code,index,new_add,updated,repeated,id,state,sel,the_page1) = funcforkick.compareindexprocess(someurl,index,new_add,updated,repeated)
        if exist_code != 0:
            (item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl,state,sel,the_page1)
            (total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=funcforkick.savingcsvforalltaskprocess(rewards,item,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)
            counts = counts + 1
        if len(total_item)>200:
            #print total_rewards_backers_distribution
            #print total_rewards_pledge_limit,total_rewards_pledged_amount
            #print
            funcforkick.projetcdata_txt_write(item,'data/middle60project/item.txt')
            funcforkick.projetcdata_txt_write(rewards,'data/middle60project/rewards.txt')
            funcforkick.index_write(index,'data/middle60project/index_value.txt','data/middle60project/index_keys.txt')
            funcforkick.writeacsvprocess('data/middle60project/project_data.csv',item_headers,total_item)
            funcforkick.writeacsvprocess('data/middle60project/rewards_backers_distribution.csv',rewards_headers,total_rewards_backers_distribution)
            funcforkick.writeacsvprocess('data/middle60project/rewards_pledge_limit.csv',rewards_headers,total_rewards_pledge_limit)
            funcforkick.writeacsvprocess('data/middle60project/rewards_pledged_amount.csv',rewards_headers,total_rewards_pledged_amount)
            #reset list
            total_item=[]
            total_rewards_backers_distribution=[]
            total_rewards_pledge_limit=[]
            total_rewards_pledged_amount=[]

            #(item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl,state,sel,the_page1)
            #(total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=funcforkick.savingcsvforalltaskprocess(rewards,item,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)
            #counts = counts + 1
            #funcforkick.projetcdata_txt_write(item,'data/middle60project/item.txt')
            #funcforkick.projetcdata_txt_write(rewards,'data/middle60project/rewards.txt')
            #funcforkick.index_write(index,'data/middle60project/index_value.txt','data/middle60project/index_keys.txt')
            #funcforkick.writeacsvprocess(saving_file,item_headers,total_item)
            #funcforkick.writeacsvprocess(rewards_backers_distribution,rewards_headers,total_rewards_backers_distribution)
            #funcforkick.writeacsvprocess(rewards_pledge_limit,rewards_headers,total_rewards_pledge_limit)
            #funcforkick.writeacsvprocess(rewards_pledged_amount,rewards_headers,total_rewards_pledged_amount)
            ##reset list
            time.sleep(0.5)
        #end = time.time()
        #conditional_insert(cursor, item)
    end = time.time()
    sys.stdout.write("\rthis spider has already read %d projects and time: %.4f/projects and  %d new add, %d updated, %d repeated" % (counts,end-start,new_add,updated,repeated))
    sys.stdout.flush()


    #return index
queue = Queue.Queue()
class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while 1:
            target = self.queue.get()
            collectingdate(target)
            self.queue.task_done()


def main(someurls):

    for j in xrange(2):
        t = ThreadClass(queue)
        t.setDaemon(True)
        t.start()
        for someurl in someurls:
            queue.put(someurl)
    queue.join()




main(someurls)


funcforkick.projetcdata_txt_write(item,'data/middle60project/item.txt')
funcforkick.projetcdata_txt_write(rewards,'data/middle60project/rewards.txt')
funcforkick.index_write(index,'data/middle60project/index_value.txt','data/middle60project/index_keys.txt')
funcforkick.writeacsvprocess('data/middle60project/project_data.csv',item_headers,total_item)
funcforkick.writeacsvprocess('data/middle60project/rewards_backers_distribution.csv',rewards_headers,total_rewards_backers_distribution)
funcforkick.writeacsvprocess('data/middle60project/rewards_pledge_limit.csv',rewards_headers,total_rewards_pledge_limit)
funcforkick.writeacsvprocess('data/middle60project/rewards_pledged_amount.csv',rewards_headers,total_rewards_pledged_amount)


print 'saving process completed'

e = time.time()
print f-e

















#if __name__=='__main__':
#    start = time.time()
#    multicore()
#    end = time.time()
#    print end-start
