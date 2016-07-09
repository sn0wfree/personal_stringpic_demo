#from PIL import Image
import pytesseract
from PIL import Image

print text
import tweepy
from TwitterSearch import *
import time
import datetime
import pandas as pd
from urllib2 import Request, urlopen, URLError
import urllib2
import requests
import requests_cache
from lxml import etree

requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)

def readcsv(file):
    with open(file,'r+') as f:
        w=pd.read_csv(file,skip_footer=1,engine='python')
    return w

def timestamp2time(timestamp):
    date=datetime.datetime.fromtimestamp(timestamp)
    return date

def rsearch_url_img(someurl):
    wasd = []
    #root_url = 'https://www.kickstarter.com'
    if someurl != '':
        try:
            response = requests.get(someurl)
            content = urllib2.urlopen(someurl).read()
            sel= etree.HTML(content)

            the_page1 = content
            print "Time: {0} / Used Cache: {1}".format(now, response.from_cache)
        except URLError as e:
            if hasattr(e, 'reason'):
                #print 'We failed to reach a server.'
                #print 'Reason: ', e.reason
                wasd =[]
            elif hasattr(e, 'code'):
                #print 'The server couldn\'t fulfill the request.'
                #print 'Error code: ', e.code
                wasd=[]
        else:
            #x= sel.xpath('//*[@id=*]/div/div[2]/div[1]/small/a/span/@data-time')
            print 1
    else:
        
        x=[]
    return x



item_headers = ['Project_ID','project_name','Goal','url',
              'pledged_amount','backers_count','creator_full_name',
              'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
              'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','launched_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']



f=readcsv('/Users/sn0wfree/Dropbox/BitTorrentSync/projectdata.csv')



image_file = 'dailypledges-5.png'
im = Image.open(image_file)
#text = pytesseract.image_to_string(im)
#text = image_file_to_string(image_file)
#text = image_file_to_string(image_file, graceful_errors=True)
#print "=====output=======\n"
#print text
text = pytesseract.image_to_string(im)
