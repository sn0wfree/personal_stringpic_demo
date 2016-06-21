
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import etree

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

    #rewardsstructure
    #rewards
    rewards_level_divided_by_goal = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/h2/span[1]/text()')

    #print rewards_level_name
    rewards_level_name = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/h3/text()')
    rewards_backers_level_distribution =sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[3]/span/text()')
    #print rewards_level.spilt()
    #rewards_level_description
    #print len(rewards_level)
    #rewards_level_description
    #initialation
    rewards_level_description =[]
    pledge_limit = []
    ship_location_info = ['0']*len(rewards_level_divided_by_goal)
    #print len(rewards_level)
    #rewards_level_description
    #ship_info
    #pledge_limit
    for i in range(1,len(rewards_level_divided_by_goal)+1):
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
    print rewards_level_name[0]
    print rewards_level_divided_by_goal[0]
    print rewards_level_description[0]
    print pledge_limit[0]
    print rewards_backers_level_distribution[0]
    #    print rrewards_level_divided_by_goal[i]]
    #process_multi_data
