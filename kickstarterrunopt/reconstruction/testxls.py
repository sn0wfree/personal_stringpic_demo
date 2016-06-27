
import time
import csv
import kickspider
from openpyxl import Workbook
import sys
import funcforkick



start = time.time()
global counts
counts = 0
global index
global total_item
global total_rewards
print 'begin to create/read index file'



#read projetc urls
file_unclear_file = open('data/allurlforkicktest1.txt','r')
file_unclear =file_unclear_file.readlines(10)
file_unclear_file.close()
index = funcforkick.index_read('data/index_value.txt','data/index_keys.txt')
total_item=[]
total_rewards=[]
file =list(set(file_unclear))
print len(file)
print 'begin to collecting data'



wb = Workbook()
ws = wb.active
lenfile = len(file)
new_add=0
updated=0
repeated=0
for i in xrange(0,lenfile):
    someurl=file[i].strip()
    if someurl !='':
        (item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl)
        (exist_code,index,new_add,updated,repeated) = funcforkick.compareindexprocess(ID,state,index,new_add,updated,repeated)
        if exist_code != 0:
            #a=(item['creator_personal_url'],item['creator_buildhistory_has_backed_projects_number'],item['Goal'],item['creator_buildhistory_has_built_projects_number'],item['creator_bio_info_url'],item['creator_Facebook_url'],item['currency'],item['duration'],item['Project_ID'],item['location_ID'],item['state_changed_at'],item['description'],item['category'],item['project_state'],item['has_a_video'],item['comments_count'],item['updates_number'],item['project_name'],item['data_percent_rasied'],item['hours_left'],item['pledged_amount'],item['creator_short_name'],item['creator_friends__facebook_number'],item['created_at'],item['Deadline'],item['backers_count'],item['creator_full_name'])
            total_item.append(item)
            total_rewards.append(rewards)
            counts = counts + 1
        if len(total_item)>10:
            for x in total_item:
                funcforkick.projetcdata_txt_write(str(x),'data/item.txt')
            for y in total_rewards:
                funcforkick.projetcdata_txt_write(str(y),'data/rewards.txt')
            #reset list
            total_item=[]
            total_rewards=[]
        sys.stdout.write("\rthis spider has already read %d projects and %d new add, %d updated, %d repeated" % (counts,new_add,updated,repeated))
        sys.stdout.flush()
        #time.sleep(1)
for x in total_item:
        funcforkick.projetcdata_txt_write(str(x),'data/item.txt')
for y in total_rewards:
        funcforkick.projetcdata_txt_write(str(y),'data/rewards.txt')

print 'saving ptoject data process completed'
print 'DGP process completed, %d new add, %d updated, %d repeated' % (counts,new_add,updated,repeated)
#print b
#funcforkick.index_write(index,'data/index_value.txt','data/index_keys.txt')
end = time.time()
print end-start
