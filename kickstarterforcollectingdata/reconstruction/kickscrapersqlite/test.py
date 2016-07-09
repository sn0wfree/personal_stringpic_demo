
import multiprocessing as mp
import sys
import funcforkick
import time
import pandas as pd
import numpy as np
import threading
import Queue
import gc



def catchup(someurl,item,rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount):

    start = time.time()
    if someurl !='':
        (id,state,sel,the_page1) = funcforkick.compareindexprocess(someurl)
        #if exist_code != 0:
        item={}
        rewards={}
        (item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl,state,sel,the_page1)
        (item,rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount)=funcforkick.savingcsvforalltaskprocess(rewards,item,item,rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount)
        counts = counts + 1
        collected.append(someurl)
        #time.sleep(1)
        end = time.time()
        #conditional_insert(cursor, item)
    sys.stdout.write("\rthis spider has already read %d projects and time: %.4f/projects " % (counts,end-start))
    sys.stdout.flush()
    return item,rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount

def resetprocess(a,item,rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount):

    if len(item)>a:
            #print rewards_backers_distribution
            #print rewards_pledge_limit,rewards_pledged_amount
            #print
        funcforkick.collected_list_overwrite(collected,have_collected_url)
            #funcforkick.projetcdata_txt_wholewrite(item,item_collect)
            #funcforkick.projetcdata_txt_wholewrite(rewards,rewards_collect)
            #funcforkick.index_write(index,'/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_value.txt','/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_keys.txt')
        funcforkick.writeacsvprocess(saving_file,item_headers,item)
        funcforkick.writeacsvprocess(rewards_backers_distribution,rewards_headers,rewards_backers_distribution)
        funcforkick.writeacsvprocess(rewards_pledge_limit,rewards_headers,rewards_pledge_limit)
        funcforkick.writeacsvprocess(rewards_pledged_amount,rewards_headers,rewards_pledged_amount)
            #reset list
        item=[]
        rewards_backers_distribution=[]
        rewards_pledge_limit=[]
        rewards_pledged_amount=[]
        gc.collect()
        time.sleep(2)
    return item,rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount
    #return index

def createurl(target_url_file,have_collected_url):
    url_list =funcforkick.read_url_file(target_url_file)
    collected=funcforkick.read_url_file(have_collected_url)
    file_lsit=list(set(url_list)-set(collected))
    file = list(set(file_lsit))
    return file
















start = time.time()

global counts
counts = 0
a=input('the ath part data collecting job:',a)
b=input('the gap for I/O:',b)
total_item=[]
total_rewards_backers_distribution=[]
total_rewards_pledge_limit=[]
total_rewards_pledged_amount=[]


print 'begin to create/read index file'
publicpath='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/slpit/split'
#112
def filepathcollection(a,publicpath):
    rewards_backers_distribution= publicpath+'/url%s/rewards_backers_distribution.csv'%a
    rewards_pledge_limit= publicpath+'/url%s/rewards_pledge_limit.csv'%a
    rewards_pledged_amount= publicpath+'/url%s/rewards_pledged_amount.csv'%a
        #item_collect='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/slpit/item.txt'
    #rewards_collect=publicpath+'/url%srewards.txt'
    saving_file = publicpath+'/url%s/project_data.csv'%a
        #index_value20='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_value.txt',
        #index_keys20='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_keys.txt'
    target_url_file= publicpath+'/url%s/url%s.txt.txt'%(a,a)
    have_collected_url= publicpath+'/url%s/collected.txt'%a
    return rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount,saving_file,target_url_file,have_collected_url

(rewards_backers_distribution,rewards_pledge_limit,rewards_pledged_amount,saving_file,target_url_file,have_collected_url) = filepathcollection(a,publicpath)

#rewards_backers_distribution=publicpath+'/url0/rewards_backers_distribution.csv'
#rewards_pledge_limit=publicpath+'/url0/rewards_pledge_limit.csv'
#rewards_pledged_amount=publicpath+'/url0/rewards_pledged_amount.csv'
    #item_collect='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/slpit/item.txt'
#rewards_collect=publicpath+'/url%srewards.txt'
#saving_file =publicpath+'/url0/project_data.csv'
    #index_value20='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_value.txt',
    #index_keys20='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/index_keys.txt'
#target_url_file=publicpath+'/url0/url0.txt.txt'
#have_collected_url=publicpath+'/url0/collected.txt'












file = createurl(target_url_file,have_collected_url)









rewards_headers=['Project_ID','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89']
item_headers = ['Project_ID','project_name','Goal','url',
          'pledged_amount','backers_count','creator_full_name',
          'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
          'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']



gc.enable()
#print 'reading urls file completed'



#



#


print 'begin to collecting data'


for someurl in file:
    (someurl,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=catchup(someurl,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)
    (b,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=resetprocess(a,total_item,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)


funcforkick.writeacsvprocess(saving_file,item_headers,total_item)
funcforkick.writeacsvprocess(rewards_backers_distribution,rewards_headers,total_rewards_backers_distribution)
funcforkick.writeacsvprocess(rewards_pledge_limit,rewards_headers,total_rewards_pledge_limit)
funcforkick.writeacsvprocess(rewards_pledged_amount,rewards_headers,total_rewards_pledged_amount)
            #reset list
        #time.sleep(1)
#funcforkick.index_write(index,index_value20,index_keys20)
print 'saving process completed'

#end = time.time()
#print end-start
