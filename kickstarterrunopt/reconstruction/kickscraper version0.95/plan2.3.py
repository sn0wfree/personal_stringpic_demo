
import multiprocessing as mp
import sys
import funcforkick
import time
import pandas as pd
import numpy as np
import threading
import Queue
import gc

import kickspideropt


def createurl(target_url_file,have_collected_url):
    url_list =funcforkick.read_url_file(target_url_file)
    collected_unclear=funcforkick.read_url_file(have_collected_url)
    collected=list(set(collected_unclear))
    print len(url_list)
    file_lsit=list(set(url_list)-set(collected))
    print len(collected)
    file = list(set(file_lsit))
    return file,collected
def filepathcollection(publicpath,url_file):
    #/Users/sn0wfree/Dropbox/BitTorrentSync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/total/collected.txt
    #publicpath='/Users/sn0wfree/Dropbox/BitTorrentSync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/total'
    rewards_backers_distribution= publicpath+'/rewards_backers_distribution.csv'
    rewards_pledge_limit= publicpath+'/rewards_pledge_limit.csv'
    rewards_pledged_amount= publicpath+'/rewards_pledged_amount.csv'
        #item_collect='/Users/sn0wfree/Dropbox/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/slpit/item.txt'
    #rewards_collect=publicpath+'/url%srewards.txt'
    saving_file = publicpath+'/project_data.csv'
        #index_value20='/Users/sn0wfree/Dropbox/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_value.txt',
        #index_keys20='/Users/sn0wfree/Dropbox/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_keys.txt'
    target_url_file= publicpath+ url_file
    have_collected_url= publicpath+'/collected.txt'
    return rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount,saving_file,target_url_file,have_collected_url



#a=input('the beginning collecting subjob is from ath :')
#b=input('the gap for I/O is:')
#c=input('the subjob will end at Job?( max 112):')
y=input('choose the number of workers for this jobs:')
#publicpath=input('please enter the document path for saving file:')
publicpath='/Users/sn0wfree/Dropbox/BitTorrentSync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/total/middle61in3_1'
#url_file=input ('please enter the target url file for starting,need add /:')
url_file='/middle61in3_1.txt'
gc.enable()

global counts
global save
counts = 0
save=0

#setup multicore system
#job_server = pp.Server()
#print 'begin to create/read index file'
def datacollectprocess(someurl):
    global total_item
    global total_rewards_backers_distribution
    global total_rewards_pledge_limit
    global total_rewards_pledged_amount
    global collected
    global counts
    global save
    global rewards_headers
    global item_headers
    global rewards_backers_distribution
    global rewards_pledge_limit
    global rewards_pledged_amount
    global saving_file
    f1 = time.time()
    if someurl !='':
        (id,state,sel,the_page1) = funcforkick.compareindexprocess(someurl)
        item={}
        rewards={}
        (item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl,state,sel,the_page1)
        (total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=funcforkick.savingcsvforalltaskprocess(rewards,item,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)
        counts = counts + 1
        if item!={}:
            collected.append(someurl)
        time.sleep(1)
    if len(total_item)>1:
            #print rewards_backers_distribution
            #print rewards_pledge_limit,rewards_pledged_amount
            #print
        funcforkick.collected_list_overwrite(collected,have_collected_url)
            #funcforkick.projetcdata_txt_wholewrite(item,item_collect)
            #funcforkick.projetcdata_txt_wholewrite(rewards,rewards_collect)
            #funcforkick.index_write(index,'/Users/sn0wfree/Dropbox/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_value.txt','/Users/sn0wfree/Dropbox/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_keys.txt')
        funcforkick.writeacsvprocess(saving_file,item_headers,total_item)
        funcforkick.writeacsvprocess(rewards_backers_distribution,rewards_headers,total_rewards_backers_distribution)
        funcforkick.writeacsvprocess(rewards_pledge_limit,rewards_headers,total_rewards_pledge_limit)
        funcforkick.writeacsvprocess(rewards_pledged_amount,rewards_headers,total_rewards_pledged_amount)
        save =save +1

            #reset list
        total_item=[]
        total_rewards_backers_distribution=[]
        total_rewards_pledge_limit=[]
        total_rewards_pledged_amount=[]
        gc.collect()
        time.sleep(y)
            #time.sleep(1)
    f2 = time.time()
    w=(len(file)-counts)*(f2-f1)/60/y
            #conditional_insert(cursor, item)
    sys.stdout.write("\rthis spider has already read/saved %d/%d projects, speed: %.4f/projects and remaining time: %.4f mins" % (counts,save*50,f2-f1,w))
    #sys.stdout.write("\rthis spider has already read %d projects" % (counts))
    sys.stdout.flush()


#for e in xrange(a,c):
    #print '\n   subjobs %s begin!'%e
#ppservers = ()

total_item=[]
total_rewards_backers_distribution=[]
total_rewards_pledge_limit=[]
total_rewards_pledged_amount=[]

#if len(sys.argv) > 1:
#    ncpus = int(sys.argv[1])
    # Creates jobserver with ncpus workers
#    job_server = pp.Server(ncpus, ppservers=ppservers)
#else:
    # Creates jobserver with automatically detected number of workers
#    job_server = pp.Server(ppservers=ppservers)




queue = Queue.Queue()
class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while 1:
            (target) = self.queue.get()
            global collected
            datacollectprocess(target)
            time.sleep(0.5)
            self.queue.task_done()



def main(file,y):

    for j in xrange(y):
        t = ThreadClass(queue)
        t.setDaemon(True)
        t.start()
    for someurl in file:

        queue.put(someurl)
    queue.join()

print '\nsubjobs  begin!'
(rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount,saving_file,target_url_file,have_collected_url) = filepathcollection(publicpath,url_file)

rewards_headers=['Project_ID','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89']
item_headers = ['Project_ID','project_name','Goal','url',
              'pledged_amount','backers_count','creator_full_name',
              'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
              'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']
(file,collected) = createurl(target_url_file,have_collected_url)
print 'begin to collecting data'
#print 'total amount is %d'%len(target_url_file)
print 'the number of left project is %d'%(len(file))

main(file,y)
funcforkick.collected_list_overwrite(collected,have_collected_url)
#(someurl,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=catchup(someurl,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)
funcforkick.writeacsvprocess(saving_file,item_headers,total_item)
funcforkick.writeacsvprocess(rewards_backers_distribution,rewards_headers,total_rewards_backers_distribution)
funcforkick.writeacsvprocess(rewards_pledge_limit,rewards_headers,total_rewards_pledge_limit)
funcforkick.writeacsvprocess(rewards_pledged_amount,rewards_headers,total_rewards_pledged_amount)
counts=0
print  '\nsubjobs completed!'






        #reset list
        #time.sleep(1)
#funcforkick.index_write(index,index_value20,index_keys20)
print 'saving process completed'

#end = time.time()
#print end-start
