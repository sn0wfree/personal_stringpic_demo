#Import the necessary methods from tweepy library
#from tweepy.streaming import StreamListener
#from tweepy import OAuthHandler
#from tweepy import Stream
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



def twittersearch_url(someurl):
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
            x= sel.xpath('//*[@id=*]/div/div[2]/div[1]/small/a/span/@data-time')
            print x
                #public_tweets = api.home_timeline()
            #x = sel.xpath('//*[@id="projects_list"]/div[*]/li[*]/div/div[2]/*/a/@href')
            #x2 = sel.xpath('//*[@id="projects_list"]/div[*]/li[*]/div/div[2]/div/a/@href')
            #x = list(set(x))
            #if x != []:
            #    a=len(x)
            #    for i in range(0,a):
            #        wasd.append(root_url +x[i])
    else:
        wasd = []
        x=[]
    return x

def readcsv(file):
    with open(file,'r+') as f:
        w=pd.read_csv(file,skip_footer=1,engine='python')
    return w

def timestamp2time(timestamp):
    date=datetime.datetime.fromtimestamp(timestamp)
    return date

item_headers = ['Project_ID','project_name','Goal','url',
              'pledged_amount','backers_count','creator_full_name',
              'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
              'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','launched_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']



f=readcsv('/Users/sn0wfree/Dropbox/BitTorrentSync/projectdata.csv')
#print f['Project_ID'][34]
#Variables that contains the user credentials to access Twitter API

#This is a basic listener that just prints received tweets to stdout.
#class StdOutListener(StreamListener):

#    def on_data(self, data):
#        print data
#        return True

#    def on_error(self, status):
#        print status


#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)


def twittercollectingprocess(keywords,launched_at,Deadline):
    counts=0
    date=launched_at
    try:
        access_token = "3337137285-i06iDwO4xGXdc2DQZ6IfTA1TISLM0KZOJ5yDkqk"
        access_token_secret = "lwdA27C0xWk9lWzwXC1EEhjS3XPkfyoEAk2DsJNycldnU"
        consumer_key = "kFZf5GK4tLj3OBKJ2NXQXdWQl"
        consumer_secret = "QOXvj2AhlI9Wxk6p5OyBxSalwcLGuM7fuXVrCBjWZKfDuCW520"


        now = datetime.date.today()
        #if created_at_add < now:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(keywords) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information
        tso.set_count(100)
        #tso.set_since_id(2016-7-1)
        tso.add_keyword(['since:%s'%launched_at,'until:%s'%Deadline])

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret
         )
        def my_callback_closure(current_ts_instance): # accepts ONE argument: an instance of TwitterSearch
            queries, tweets_seen = current_ts_instance.get_statistics()
            if queries > 0 and (queries % 5) == 0: # trigger delay every 5th query
                time.sleep(60) # sleep for 60 seconds

         # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
            counts+=1
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

    return counts,date


#'https://twitter.com/search?q=The%20Music%20Box%20Village%20finds%20a%20home!&src=typd'
#print type(f['project_name'][1]),f['project_name'][1],type(''.join(f['project_name'][1]))
keywords=[f['project_name'][1000]]
#print keywords
#print f['Deadline'][1000],f['launched_at'][1000]
deadline=timestamp2time(float(f['Deadline'][1000])).date()
launched_at=timestamp2time(float(f['launched_at'][1000])).date()
#print deadline,launched_at
(counts,date)=twittercollectingprocess(keywords,launched_at,deadline)
print 'date:%s, has %d tweets'%(date,counts)

now = datetime.date.today()
#print now
#https://twitter.com/search?q=%22Help%20spread%20a%20positive%20message%20about%20ICELAND%22%20since%3A2010-02-06%20until%3A2010-03-22&src=typd
#xpath('//*[@id="stream-item-tweet-9134776352"]/div/div[2]/div[1]/small/a/span/text()')
#xpath('//*[@id="stream-item-tweet-9484249963"]/div/div[2]/div[1]/small/a/span/text()')
#xpath('//*[@id="stream-item-tweet-9010492582"]/div/div[2]/div[1]/small/a/span/text()')
    #public_tweets = api.home_timeline()


a='https://twitter.com/search?q=The%20Music%20Box%20Village%20finds%20a%20home!&src=typd'
w=twittersearch_url(a)

    #for tweet in public_tweets:
    #    print tweet.text

    #stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['The Music'])
