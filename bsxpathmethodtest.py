
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import etree
#from twisted.enterprise import adbapi
#import MySQLdb
#import MySQLdb.cursors

def retype(x):
    x_new = ''.join(x)
    return x_new


names = locals()
someurl = 'https://www.kickstarter.com/projects/neliobarros/nixin-typeface?ref=discover_potd'
root_url = 'https://www.kickstarter.com'
try:
      response = Request(someurl)
      content = urllib2.urlopen(someurl).read()
      sel= etree.HTML(content)
      ##this is for some data without tab.
      req = urlopen(response)
      the_page1 = req.readlines()
except URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:

    def OnlyStr(s,oth=''):
       #s2 = s.lower();
       fomart = 'abcdefghijklmnopqrstuvwxyz0123456789:,'
       for c in s:
           if not c in fomart:
               s = s.replace(c,'');
       return s;
    #print(OnlyStr(a))
    #change type of list
    #rewardsstructure
    data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')
    data_pool_url = ''.join(str(x) for x in data_pool_url)
    #print data_pool_url
    #turn to new websites
    #new data form
    for line in the_page1:
        #project_ID_str
        if 'data'  in line:
            words = line.split('" ')
            for word in words:
                if 'data class="Project' in word:
                    project_ID_str = word.split('Project')[1]
    data_pool_url_websites = urllib2.urlopen(data_pool_url).read()
    data_pool_url_websites = ''.join(str(x) for x in data_pool_url_websites)
    a = data_pool_url_websites#.split(',')
    #print a
    name =[]
    #transfor list to dictionary

    b = OnlyStr(a).strip('project:')
    #print len(b.split(','))
    for i in range(0,len(b.split(','))):
        name.append(b.split(',')[i].split(':'))
    dics = dict(name)

    #rewards
    rewards_level_divided_by_goal = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/h2/span[1]/text()')

    #print rewards_level_name
    rewards_level_name = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/h3/text()')
    rewards_backers_level_distribution =sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[3]/span[@class="pledge__backer-count"]/text()')
    #print rewards_level.spilt()
    #rewards_level_description
    #print len(rewards_level)
    #rewards_level_description
    #initialation
    rewards_level_description =[]
    pledge_limit = []
    ship_location_info = ['0']*len(rewards_level_divided_by_goal)
    #print len(rewards_level)
    #print len(rewards_level_divided_by_goal)
    #rewards_level_description
    #ship_info
    #pledge_limit
    for i in range(1,len(rewards_level_divided_by_goal)):
        #print i
        c = str(i)
        #rewards_level_description
        rewards_level_description_a= '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li['
        rewards_level_description_b = ']/div[2]/div[1]/p/text()'
        #pledge_limit for each part of pledges
        pledge_limit_a= '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li['
        pledge_limit_b = ']/div[2]/div[3]//span[@class="pledge__limit"]/text()'
        #ship_info
        ship_location_info_a = '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li['
        ship_location_info_b =']/div[2]/div[2]/div[2]/span[2]/text()'
        #combin the xpath for each variable
        pledge_limit_a += c
        pledge_limit_a += pledge_limit_b
        ship_location_info_a += c
        ship_location_info_a += ship_location_info_b
        rewards_level_description_a += c
        rewards_level_description_a += rewards_level_description_b
        #declare the empty list
        rewards_level_description_split_list=[]
        pledge_limit_split_list=[]
        ship_location_info_list=[]
        #split each variable
        #rewards_level_description
        rewards_level_description_split_list = sel.xpath(rewards_level_description_a)
        rewards_level_description_split = rewards_level_description_split_list
        rewards_level_description_split =''.join(rewards_level_description_split)
        rewards_level_description.append(rewards_level_description_split)
        #pledge_limit
        pledge_limit_split_list = sel.xpath(pledge_limit_a)
        pledge_limit_split = pledge_limit_split_list
        pledge_limit_split =''.join(pledge_limit_split)
        pledge_limit.append(pledge_limit_split)
        #ship_location_info
        ship_location_info_split_list = sel.xpath(ship_location_info_a)
        ship_location_info_split = ship_location_info_split_list
        #print ship_location_info_split, ship_location_info_split_list
        ship_location_info_split =''.join(ship_location_info_split)
        ship_location_info_split= str(ship_location_info_split)
        #ship_location_info[i-1] = ship_location_info_split



    #multi_data
    #print 'rewards_level_divided_by_goal:' ,rewards_level_divided_by_goal


    #print 'rewards_level_name:' ,rewards_level_name
    #print 'rewards_level_description:' ,rewards_level_description
    #print 'pledge_limit:' , pledge_limit
    #for i in range(0,len(rewards_level):
    #print rewards_backers_level_distribution
    #print ''.join(rewards_level_name)
    #print retype(rewards_level_name)
    #print retype(rewards_level_divided_by_goal)
    #print rewards_level_description[0]
    #print pledge_limit[0]
    #print rewards_backers_level_distribution[0]
    #    print rrewards_level_divided_by_goal[i]]
    #process_multi_data
    #regroup
    item = {}
    level_rewards_by_goal={}
    level_rewards_by_backers_distribution={}
    level_rewards_by_pledge_limit={}
    level_rewards_by_description={}
    level_rewards_by_name={}
    a=[]

    #obb = ['name','pledged','description','pledge_limit','backers_distribution']
    for i in range(1,len(rewards_level_divided_by_goal)+1):
        print i
        a.append(i)
    print a
    level_rewards_name_backers=dict(zip((rewards_level_name,rewards_backers_level_distribution)))
    level_rewards_by_goal=dict(zip(a,rewards_level_divided_by_goal))
    level_rewards_by_backers_distribution=dict(zip(a,rewards_backers_level_distribution))
    level_rewards_by_pledge_limit=dict(zip(a,pledge_limit))
    level_rewards_by_description=dict(zip(a,rewards_level_description))
    level_rewards_by_name=dict(zip(a,rewards_level_name))
    #print rewards
    level_rewards_by_goal["project ID"]= project_ID_str
    level_rewards_by_backers_distribution["project ID"]= project_ID_str
    level_rewards_by_pledge_limit["project ID"]= project_ID_str
    level_rewards_by_description["project ID"]= project_ID_str
    level_rewards_by_name["project ID"]= project_ID_str
    print level_rewards_by_goal, level_rewards_by_backers_distribution, level_rewards_by_pledge_limit, level_rewards_by_description, level_rewards_by_name
        #names['rewards_name_level%s' % 0 ] = ''
        #names['rewards_name_level%s' % i] = rewards_level_name[i]
        #names['rewards_pledged_goal_level%s' % i] = rewards_level_divided_by_goal[i]
        #names['rewards_description_level%s' % i] = rewards_level_description[i]
        #names['rewards_pledge_limit_level%s' % i] = pledge_limit[i]
        #names['rewards_backers_distribution_level%s' % i] = rewards_backers_level_distribution[i]
        #item = dict(['rewards_name_level%s' % i]= str(rewards_level_name[i]))
    #rewards_rewards_name_levellen(rewards_level_divided_by_goal)
    print item

        #
        #names['rewards_pledged_level_%s' % i+1 ] =rewards_level_divided_by_goal[i]
        #names['rewards_description_level_%s' % i+1 ] =rewards_level_description[i]
        #names['rewards_pledge_limit_level_%s' % i+1 ] =pledge_limit[i]
        #names['rewards_backers_distribution_level_%s' % i+1 ] =rewards_backers_level_distribution[i]
        #print  names['rewards_level_%s_%f' % i+1 % obb ]
