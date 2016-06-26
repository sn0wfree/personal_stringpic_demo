import csv
import kickspider
import sys
import funcforkick
import time
import pandas as pd
import numpy as np

start = time.time()

global counts
counts = 0


global index
global total_item
global total_rewards

print 'begin to create/read index file'
#read projetc urls
file_unclear_file = open('data/allurlforkicktest.txt','r+')
file_unclear =file_unclear_file.readlines()
file_unclear_file.close()
index = funcforkick.index_read('data/index_value20.txt','data/index_keys20.txt')

w='a'


saving_file ='data/project_data.csv'
rewards_headers=['Project_ID','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
item_headers = ['Project_ID','project_name','Goal',
          'pledged_amount','backers_count','creator_full_name',
          'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
          'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number','created_at','Deadline']
total_item=[]
total_rewards_backers_distribution=[]
total_rewards_pledge_limit=[]
total_rewards_pledged_amount=[]
project_data='data/project_data.csv'
rewards_backers_distribution='data/rewards_backers_distribution.csv'
rewards_pledge_limit='data/rewards_pledge_limit.csv'
rewards_pledged_amount='data/rewards_pledged_amount.csv'
file =list(set(file_unclear))
new_add=0
updated=0
repeated=0
#print 'reading urls file completed'
print 'begin to collecting data'
for someurl in file:
    if someurl !='':
        someurl=someurl.strip()
        (item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl)
        global new_add
        global updated
        global repeated
        (exist_code,index,new_add,updated,repeated) = funcforkick.compareindexprocess(ID,state,index,new_add,updated,repeated)
        if exist_code != 0:
            (total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=funcforkick.savingcsvforalltaskprocess(rewards,item,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)
            counts = counts + 1
            funcforkick.projetcdata_txt_write(item,'data/item.txt')
            funcforkick.projetcdata_txt_write(rewards,'data/rewards.txt')
        if len(total_item)>10:
            funcforkick.writeacsvprocess(saving_file,w,item_headers,total_item)
            funcforkick.writeacsvprocess(rewards_backers_distribution,w,rewards_headers,total_rewards_backers_distribution)
            funcforkick.writeacsvprocess(rewards_pledge_limit,w,rewards_headers,total_rewards_pledge_limit)
            funcforkick.writeacsvprocess(rewards_pledged_amount,w,rewards_headers,total_rewards_pledged_amount)
            #reset list
            total_item=[]
            total_rewards_backers_distribution=[]
            total_rewards_pledge_limit=[]
            total_rewards_pledged_amount=[]
        #conditional_insert(cursor, item)
    sys.stdout.write("\rthis spider has already read %d projects and %d new add, %d updated, %d repeated" % (counts,new_add,updated,repeated))
    sys.stdout.flush()
        #time.sleep(1)
funcforkick.index_write(index,'data/index_value20.txt','data/index_keys20.txt')
#end = time.time()
#print end-start
