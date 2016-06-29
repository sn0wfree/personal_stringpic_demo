import unicodecsv
import kickspider
import funcforkick



def writeacsvprocess(file,item,headers):
    with open(file,'r+') as project_data:
        project_data_read_csv = unicodecsv.reader(project_data,headers)
        if not headers in project_data_read_csv:
            status=0
        else:
            status=1
        print status
    with open(file,'a') as project_data:
        project_data_csv = unicodecsv.DictWriter(project_data,headers)
        if status ==0:
            project_data_csv.writeheader()
        project_data_csv.writerows(item)

item=[]
someurl1='https://www.kickstarter.com/projects/hypnotistcollector/coins-of-the-forge-candle-set-with-embedded-metal?ref=category_featured'
someurl2='https://www.kickstarter.com/projects/spicecrafters/the-ultimate-seafood-sauce-tampa-bay-crab-chilau?ref=category_featured'
(item1,b1,c1,d1)=kickspider.webscraper_live(someurl1)
(item2,b2,c2,d2)=kickspider.webscraper_live(someurl2)
item.append(item1)
item.append(item2)

item_headers = ['Project_ID','project_name','Goal','url',
          'pledged_amount','backers_count','creator_full_name',
          'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
          'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']

#item=[]
file='/Users/sn0wfree/BitTorrentSync/kickstarterscrapy/kickstarterrunopt/reconstruction/kickscraper version0.95/test.csv'
funcforkick.writeacsvprocess(file,item_headers,item)
