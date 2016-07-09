import datetime
import time
import unicodecsv
import pandas as pd

def readcsv(file):
    with open(file,'r+') as f:
        w=pd.read_csv(file,skip_footer=1,engine='python')
    return w



item_headers = ['Project_ID','project_name','Goal','url',
              'pledged_amount','backers_count','creator_full_name',
              'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
              'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','launched_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']



f=readcsv('/Users/sn0wfree/Dropbox/BitTorrentSync/projectdata.csv')

print len(f)
print f['Project_ID'][34]
now =  datetime.datetime.today()
now_date=now.date()
now_str=now.strftime("%Y-%m-%d")
#print type(now_str),now_str,now
date='2016-07-08'
created_at_timestamp = 1413847260

Deadline_timestamp = 1423550843

timestamp = time.mktime(now.timetuple())

def timestamp2time(timestamp):
    date=datetime.datetime.fromtimestamp(timestamp).date()
    return date
#print timestamp2time(created_at_timestamp)
#print timestamp2time(Deadline_timestamp)
def time2timestamp(time):
    timestamp = time.mktime(time.timetuple())
    return timestamp

print now
#tt=time2timestamp(now)
#print tt
