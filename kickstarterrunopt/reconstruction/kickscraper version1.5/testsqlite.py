
import csv
import kickspider
import funcforkick
import time
import shelve
import sqlite3
from collections import defaultdict

start = time.time()
projectdata = sqlite3.connect("projectdatatest.db")
cur = projectdata.cursor()
projectdata_create_table = "create table projectdata (creator_personal_url text, creator_buildhistory_has_backed_projects_number text, Goal text, creator_built_projects_number text, creator_bio_info_url text, creator_Facebook_url text, currency text, duration text, Project_ID text, location_ID text, state_changed_at text, description text, category text, project_state text, has_a_video text, comments_count test, updates_number test, project_name text, data_percent_rasied text, hours_left text, pledged_amount text, creator_short_name text, creator_friends__facebook_number text, created_at text, Deadline int, backers_count int, creator_full_name text)"
#if not exist
#cur.execute(projectdata_create_table )


def addvalue(cur,projectdata_add):
    cur.executemany('insert into projectdata values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', defaultdict(None,projectdata_add))
    projectdata.commit()




proejectrewards =sqlite3.connect("projectrewards.db")


def buildupasqlite(file,name,prject_item_content):
    name = sqlite3.connect(file)
    cur = name.cursor()
    return cur


#create_table = "create table projetcdata (%s) " % prject_item_content

#cur.execute(create_table)

total_item=[]
total_rewards=[]

#file_items = open('item.txt','r').readlines()
#file_rewards = open('rewards.txt','r').readlines()
def read_item(file_item):
    for file_item in file_items:
        file_item =file_item.split('};')
        for items in file_item:
            items =items.strip('{')
            for item in items:
                item = item.strip("','")
                for words in item:
                    words = words.strip("':'")
                    #print len(words)
                    #dict_item[words[0]]=words[1]
someurls=[]
#for live
someurls.append('https://www.kickstarter.com/projects/neliobarros/nixin-typeface?ref=discover_potd')
#for cancelled
someurls.append( 'https://www.kickstarter.com/projects/usagraphicsfest/usa-graphic-design-festival?ref=category_newest')
#for unseccessful
someurls.append('https://www.kickstarter.com/projects/captainblacksbbq/captain-blacks-barbecue?ref=category_newest')
someurls.append('https://www.kickstarter.com/projects/1708738346/the-searzall')
total_item10=[]
for someurl in someurls:
    if someurl !='':
        (item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl)



        a=(item['creator_personal_url'],item['creator_buildhistory_has_backed_projects_number'],item['Goal'],item['creator_built_projects_number'],item['creator_bio_info_url'],item['creator_Facebook_url'],item['currency'],item['duration'],item['Project_ID'],item['location_ID'],item['state_changed_at'],item['description'],item['category'],item['project_state'],item['has_a_video'],item['comments_count'],item['updates_number'],item['project_name'],item['data_percent_rasied'],item['hours_left'],item['pledged_amount'],item['creator_short_name'],item['creator_friends_facebook_number'],item['created_at'],item['Deadline'],item['backers_count'],item['creator_full_name'])
        print len(a)


        total_item10.append(a)
        #if len(total_item10) > 2:
        addvalue(cur,a)
        total_item10=[]
        total_rewards.append(rewards)
addvalue(cur,total_item10)
#(item,rewards,ID,state)= funcforkick.datagenerateprocess(someurls[0])
#items_headers =['creator_personal_url', 'creator_buildhistory_has_backed_projects_number', 'Goal', 'creator_built_projects_number', 'creator_bio_info_url', 'creator_Facebook_url', 'currency', 'duration', 'Project_ID', 'location_ID', 'state_changed_at', 'description', 'category', 'project_state', 'has_a_video', 'comments_count', 'updates_number', 'project_name', 'data_percent_rasied', 'hours_left', 'pledged_amount', 'creator_short_name', 'creator_friends_facebook_number', 'created_at', 'Deadline', 'backers_count', 'creator_full_name']
#rewards_headers=['rewards_backers_level_distribution', 'rewards_level_description', 'rewards_level_divided_by_goal', 'pledge_limit', 'rewards_level_name', 'Project_ID']
#print list(item)
#print list(rewards)


#def writeacsvfile(headers,item,writeFileName):
#    with open(writeFileName, mode='a', newline='') as wf:

#            writer = csv.DictWriter(wf, headers)
#            writer.writeheader()
#            writer.writerows(item)
#    wf.close()

#writeacsvfile(headers,item,writeFileName)












cur.execute('select * from projectdata')

print cur.fetchall()





#print len(total_item),len(total_rewards)
end = time.time()
print end-start


#print dict_item
