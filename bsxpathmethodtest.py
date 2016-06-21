
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
    #rewards
    #print rewards_level
    rewards_level = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/h2/span[1]/text()')
    #print rewards_level
    #print len(rewards_level)
    rewards_level_name = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/h3/text()')
    #print rewards_level_name


    #def rerange_xpath(,oth=''):
       #s2 = s.lower();
     #  fomart = 'abcdefghijklmnopqrstuvwxyz0123456789:,'
      # for c in s:
        #   if not c in fomart:
        #       s = s.replace(c,'');
       #return s;
    #print(OnlyStr(a))
    #rewards_level_description
    #for i in range(1,len(rewards_level)+1):
        #print i
    #    a= '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li['
    #    b = ']/div[2]/div[1]/p/text()'
    #    c = str(i)
        #print c
    #    a += c
    #    a += b
        #print a
    #    rewards_level_description_split_list=[]
        #rewards_level_description_split_list = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[1]/p/text()')
    #    rewards_level_description_split_list = sel.xpath(a)
    #    rewards_level_description_split = rewards_level_description_split_list
    #    rewards_level_description_split =''.join(rewards_level_description_split)
    #    rewards_level_description.append(rewards_level_description_split)
    #print rewards_level_description
    #print len(rewards_level_description)
    rewards_level_estimated_delivery = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[2]/div/span[2]/time/text()')
    print rewards_level_estimated_delivery
    #rewards_level_backers_number
    rewards_level_backers_number =sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[3]//span[@class="pledge__backer-count"]/text()')
    print rewards_level_backers_number
    #pledge__limit
    pledge_limit = []
    #ship_location_info
    ship_location_info = ['0']*9
    for i in range(1,len(rewards_level)+1):
        #print i
        pledge_limit_a= '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li['
        pledge_limit_b = ']/div[2]/div[3]//span[@class="pledge__limit"]/text()'
        pledge_limit_c = str(i)
        ship_location_info_a = '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li['
        ship_location_info_b =']/div[2]/div[2]/div[2]/span[2]/text()'
        ship_location_info_c = str(i)
        #print c
        pledge_limit_a += pledge_limit_c
        pledge_limit_a += pledge_limit_b
        ship_location_info_a += ship_location_info_c
        ship_location_info_a += ship_location_info_b
            #print a
        pledge_limit_split_list=[]
        ship_location_info_list=[]
        pledge_limit_split_list = sel.xpath(pledge_limit_a)
        pledge_limit_split = pledge_limit_split_list
        pledge_limit_split =''.join(pledge_limit_split)
        pledge_limit.append(pledge_limit_split)
        ship_location_info_split_list = sel.xpath(ship_location_info_a)
        ship_location_info_split = ship_location_info_split_list
        #print ship_location_info_split, ship_location_info_split_list
        ship_location_info_split =''.join(ship_location_info_split)
        ship_location_info[i-1]= str(ship_location_info_split)
    print 'pledge__limit:' , pledge_limit
    print 'ship_location_info:' , ship_location_info
    #a = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[2]/div[2]/span[2]')
    #print a

    #//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[7]/div[2]/div[3]/span
    #//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[9]/div[2]/div[3]/span[3]





#creator_friends__facebook_number_potential =
