import csv
import kickspider
import sys
import funcforkick
import time
import pandas as pd
import numpy as np





start = time.time()
someurls=[]
#someurl = 'https://www.kickstarter.com/projects/neliobarros/nixin-typeface?ref=discover_potd'
someurls.append('https://www.kickstarter.com/projects/neliobarros/nixin-typeface?ref=discover_potd')
#for cancelled
someurls.append( 'https://www.kickstarter.com/projects/usagraphicsfest/usa-graphic-design-festival?ref=category_newest')
#for unseccessful
someurls.append('https://www.kickstarter.com/projects/captainblacksbbq/captain-blacks-barbecue?ref=category_newest')
someurls.append('https://www.kickstarter.com/projects/1708738346/the-searzall')





#with open('project_data.csv') as project_data:
#    project_data_csv= csv.dictreader(project_data)


#for row in projectdata_csv:

rewards_headers=['Project_ID','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']


item_headers = ['Project_ID','project_name','Goal',
          'pledged_amount','backers_count','creator_full_name',
          'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
          'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number','created_at','Deadline']
total_item=[]
total_rewards_backers_distribution=[]
total_rewards_pledge_limit=[]
total_rewards_pledged_amount=[]
for someurl in someurls:
    (total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=funcforkick.savingcsvforalltaskprocess(someurl,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)



#rewards_list=['rewards_backers_level_distribution', 'rewards_level_description', 'rewards_level_divided_by_goal', 'pledge_limit', 'rewards_level_name', 'Project_ID']

project_data='data/project_data.csv'
rewards_backers_distribution='data/rewards_backers_distribution.csv'
rewards_pledge_limit='data/rewards_pledge_limit.csv'
rewards_pledged_amount='data/rewards_pledged_amount.csv'


w='w'
funcforkick.writeacsvprocess(project_data,w,item_headers,total_item)
funcforkick.writeacsvprocess(rewards_backers_distribution,w,rewards_headers,total_rewards_backers_distribution)
funcforkick.writeacsvprocess(rewards_pledge_limit,w,rewards_headers,total_rewards_pledge_limit)
funcforkick.writeacsvprocess(rewards_pledged_amount,w,rewards_headers,total_rewards_pledged_amount)
#writeacsvprocess

#with open('data/project_data.csv','w') as project_data:
#    project_data_csv = csv.DictWriter(project_data, rewards_headers)
#    project_data_csv.writeheader()
#    project_data_csv.writerows(total_item)
    #project_data_csv.writerows(item)





#(item['creator_personal_url'],item[' creator_buildhistory_has_backed_projects_number'],item[' Goal'],item[' creator_buildhistory_has_built_projects_number'],item[' creator_bio_info_url'],item[' creator_Facebook_url'],item[' currency'],item[' duration'],item[' Project_ID'],item[' location_ID'],item[' state_changed_at'],item[' description'],item[' category'],item[' project_state'],item[' has_a_video'],item[' comments_count'],item[' updates_number'],item[' project_name'],item[' data_percent_rasied'],item[' hours_left'],item[' pledged_amount'],item[' creator_short_name'],item[' creator_friends__facebook_number'],item[' created_at'],item[' Deadline'],item[' backers_count'],item[' creator_full_name'])



#writer = csv.writer(sys.stdout)

#for item in



#projecy_rewards_data = wb.create_sheet()

#project_data.title = 'prject_data_basic_info'
#print wb.get_sheet_names()

#lenitem =len(item)
#def :
#    cells = project_data['A1':'A27']


















#funcforkick.index_write(index,'data/index_value.txt','data/index_keys.txt')
end = time.time()
print end-start
