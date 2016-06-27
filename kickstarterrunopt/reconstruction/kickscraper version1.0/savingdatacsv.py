

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
file_unclear_file = open('data/first20project/first20project.txt','r+')
file_unclear =file_unclear_file.readlines()
file_unclear_file.close()
index = funcforkick.index_read('data/first20project/index_value20.txt','data/first20project/index_keys20.txt')

w='a'


saving_file ='data/first20project/project_data.csv'
rewards_headers=['Project_ID','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50']
item_headers = ['Project_ID','project_name','Goal','url',
          'pledged_amount','backers_count','creator_full_name',
          'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
          'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']
total_item=[]
total_rewards_backers_distribution=[]
total_rewards_pledge_limit=[]
total_rewards_pledged_amount=[]
rewards_backers_distribution='data/first20project/rewards_backers_distribution.csv'
rewards_pledge_limit='data/first20project/rewards_pledge_limit.csv'
rewards_pledged_amount='data/first20project/rewards_pledged_amount.csv'
file =list(set(file_unclear))
new_add=0
updated=0
repeated=0
#print 'reading urls file completed'
print 'begin to collecting data'
for someurl in file:
    start = time.time()
    if someurl !='':
        someurl=someurl.strip()
        global new_add
        global updated
        global repeated
        (exist_code,index,new_add,updated,repeated,id,state,sel,the_page1) = funcforkick.compareindexprocess(someurl,index,new_add,updated,repeated)
        if exist_code != 0:
            (item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl,state,sel,the_page1)
            (total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=funcforkick.savingcsvforalltaskprocess(rewards,item,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)
            counts = counts + 1
        if len(total_item)>100:
            #print total_rewards_backers_distribution
            #print total_rewards_pledge_limit,total_rewards_pledged_amount
            #print
            funcforkick.projetcdata_txt_write(item,'data/first20project/item.txt')
            funcforkick.projetcdata_txt_write(rewards,'data/first20project/rewards.txt')
            funcforkick.index_write(index,'data/first20project/index_value20.txt','data/first20project/index_keys20.txt')
            funcforkick.writeacsvprocess(saving_file,item_headers,total_item)
            funcforkick.writeacsvprocess(rewards_backers_distribution,rewards_headers,total_rewards_backers_distribution)
            funcforkick.writeacsvprocess(rewards_pledge_limit,rewards_headers,total_rewards_pledge_limit)
            funcforkick.writeacsvprocess(rewards_pledged_amount,rewards_headers,total_rewards_pledged_amount)
            #reset list
            total_item=[]
            total_rewards_backers_distribution=[]
            total_rewards_pledge_limit=[]
            total_rewards_pledged_amount=[]
            time.sleep(5)
        end = time.time()
        #conditional_insert(cursor, item)
    sys.stdout.write("\rthis spider has already read %d projects and time: %.4f/projects and  %d new add, %d updated, %d repeated" % (counts,end-start,new_add,updated,repeated))
    sys.stdout.flush()



funcforkick.writeacsvprocess(saving_file,item_headers,total_item)
funcforkick.writeacsvprocess(rewards_backers_distribution,rewards_headers,total_rewards_backers_distribution)
funcforkick.writeacsvprocess(rewards_pledge_limit,rewards_headers,total_rewards_pledge_limit)
funcforkick.writeacsvprocess(rewards_pledged_amount,rewards_headers,total_rewards_pledged_amount)
            #reset list
        #time.sleep(1)
funcforkick.index_write(index,'data/first20project/index_value20.txt','data/first20project/index_keys20.txt')
print 'saving process completed'

#end = time.time()
#print end-start
