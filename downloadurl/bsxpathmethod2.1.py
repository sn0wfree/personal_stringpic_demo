
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import etree
#someurl = 'https://www.kickstarter.com/projects/neliobarros/nixin-typeface?ref=discover_potd'
someurl = 'https://www.kickstarter.com/projects/1060627644/35000-years-in-the-making-pens-made-from-ancient-k?ref=category_featured'
root_url = 'https://www.kickstarter.com'

def OnlyStr(s,oth=''):
   #s2 = s.lower();
   fomart = 'abcdefghijklmnopqrstuvwxyz0123456789:,'
   for c in s:
       if not c in fomart:
           s = s.replace(c,'');
   return s;
#print(OnlyStr(a))
#change type of list
def retype(x):
    x_new = ''.join(x)
    return x_new
names = locals()

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

    #project_name
    project_name_str = sel.xpath('//*[@id="content-wrap"]/section/div[1]/div/h2/a/text()')
    project_name = ''.join(project_name_str)
    #projetc_ID
    #created_at/setupdate
    #deadline_quot
    #createddate/set up date
    for line in the_page1:
        #project_ID_str
        if 'data'  in line:
            words = line.split('" ')
            for word in words:
                if 'data class="Project' in word:
                    project_ID_str = word.split('Project')[1]
        #created_at/setupdate
        if 'created_at&quot;:' in line:
            words = line.split(',&quot;')
            for word in words:
                if 'created_at' in word:
                    created_at_str = word.split('&quot;:')[1]

        #state_changed_at
        #if 'state_changed_at&quot:' in line:
        #    words = line.split(',&quot;')
        #    for word in words:
        #        if 'state_changed_at' in word:
        #            state_changed_at_str= word.split('&quot;:')[1]
        #deadline_quot
        if 'deadline&quot;:' in line:
            words = line.split(',&quot;')
            for word in words:
                if 'deadline' in word:
                    deadline_quot_str = word.split('&quot;:')[1]
        if 'ref=category"><span aria-hidden' in line:
            words = line.split('"')
            for word in words:
                if '?ref=category' in word:
                    discover_category =  word.split('?ref=category')[0]
                    category = discover_category.rsplit('/discover/categories/')[1]



    #location_id
    #createddate/set up date
    location_id_str = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[1]/div[2]/div[1]/div/a[1]/text()')
    location_id =''.join(location_id_str)
    project_ID = ''.join(project_ID_str)
    created_at=''.join(created_at_str)
    #state_changed_at=''.join(state_changed_at_str)
    deadline_quot=''.join(deadline_quot_str)





    #backers_count
    backers_count= sel.xpath('//*[@id="backers_count"]/data/text()')


    #goal
    goal = sel.xpath('//*[@id="stats"]/div/div[2]/span/span[1]/text()')

    #pledged_amount
    pledged_amount = sel.xpath('//*[@id="pledged"]/data/text()')
    #data_percent_rasied
    data_percent_rasied = sel.xpath('//*[@id="pledged"]/@data-percent-raised')
    #data-currency
    currency = sel.xpath('//*[@id="pledged"]/data/@data-currency')

    #data_poll_url
    data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')

    #setup date
    #setup_date = sel.xpath('')
    #hours_left
    hours_left = sel.xpath('//*[@id="project_duration_data"]//@data-hours-remaining')
    #day_left
    day_left = sel.xpath('//*[@id="stats"]/div/div[3]/div/div/div/text()')
    #data-duration
    data_duration = sel.xpath('//*[@id="project_duration_data"]//@data-duration')


    #updates
    updates = sel.xpath('//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[3]/span/text()')


    #rewardsstructure
    #rewards
    rewards_level_divided_by_goal = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/h2/span[1]/text()')

    #print rewards_level_name
    rewards_level_name = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/h3/text()')
    rewards_backers_level_distribution =sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[3]/span[@class="pledge__backer-count"]/text()')
    #rewards_backers_level_distribution =sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[3]/span[3]')
    #print rewards_level.spilt()
    #rewards_level_description
    #print len(rewards_level)
    #rewards_level_description
    #initialation
    rewards_level_description =[]
    pledge_limit = []
    #ship_location_info
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

    #deadline
    deadline_xpath= sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[1]/div/div/p/time/text()')

    #project_description
    description = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[1]/div[2]/p/text()')


    #url

    #creator_info_hub
    #creator_short_name
    creator_short_name = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/h5/a/text()')



    #creator_url
    creator_personal_url = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/div[3]/div/div[2]/p/a//@href')

    #creator_bio_info
    creator_bio_info_shorturl_list = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/p/a[1]//@href')

    creator_bio_info_url = root_url + ''.join(str(x) for x in creator_bio_info_shorturl_list)

    #turn to new creator_bio_websites
    creator_bio_info = urllib2.urlopen(creator_bio_info_url).read()
    creator_bio_info_sel= etree.HTML(creator_bio_info)
    creator_full_name = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[1]/span/span[2]/text()')



    #creator_buildhistory
    creator_buildhistory_has_backed_projects_number = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[4]/a/text()')
    creator_buildhistory_has_built_projects_number = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[4]/text()')
    built_projects_number_list = creator_buildhistory_has_built_projects_number
    backed_projects_number_list = creator_buildhistory_has_backed_projects_number
    creator_buildhistory_has_built_projects_number = "".join(built_projects_number_list).strip()
    creator_buildhistory_has_backed_projects_number = "".join(backed_projects_number_list).strip()


    #facebook information
    creator_friends__facebook_number_potential = str(creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/text()'))
    if 'Not connected' in creator_friends__facebook_number_potential:
        creator_friends__facebook_number = 'Not connected'
        creator_Facebook_url = 'Not connected'
    else:
        creator_Facebook_url= creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/span[2]/a//@href')
        creator_friends__facebook_number_str = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/span[2]/a/text()')
        creator_friends__facebook_number = ''.join(creator_friends__facebook_number_str)


    data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')
    data_pool_url = ''.join(str(x) for x in data_pool_url)

    #print data_pool_url
    #turn to new websites
    #new data form
    data_pool_url_websites = urllib2.urlopen(data_pool_url).read()
    data_pool_url_websites = ''.join(str(x) for x in data_pool_url_websites)
    a = data_pool_url_websites#.split(',')
    #print a
    name =[]
    #transfor list to dictionary
    b = OnlyStr(a).strip('project:')
    for i in range(0,len(b.split(','))):
        name.append(b.split(',')[i].split(':'))
    dics = dict(name)
    #print dics
    #print 'value: %s' % dics.items()

    state = dics['state']
    pledged = dics ['pledged']
    state_changed_at = dics['statechangedat']
    comments_count = dics['commentscount']
    id = dics['id']

#def regrouptype(x):
#    x_new = ''.join(x)
#    return x_new
    #data_structure_change
    deadline_date= ''.join(deadline_xpath)
    backers_count_str = ''.join(backers_count)
    goal_str = ''.join(goal)
    pledged_amount_str =''.join(pledged_amount)
    currency_str = ''.join(currency)
    data_percent_rasied_str = ''.join(data_percent_rasied)
    hours_left_str = ''.join(hours_left)



    print 'project_name:', project_name
    print 'location_ID:', location_id
    print 'Project ID:', project_ID
    #print 'Project ID:', id
    print 'projetc_state:' , state
    print 'category:', category
    print 'created_at:',created_at
    print 'Deadline:',deadline_quot
    #print 'deadline_xpath:', deadline_date
    print 'state_changed_at:',state_changed_at

    print 'backers count:', backers_count_str
    #print 'backers_count:',  dics['backerscount']
    print 'Goal:', goal_str
    print 'pledged_amount',pledged_amount_str
    #print 'pledged:', pledged
    print 'data_percent_rasied:', data_percent_rasied_str
    print 'currency:', currency_str
    print 'hours_left:', hours_left_str
    #print 'day_left:', day_left


    print 'description:',''.join(description)
    print 'creator_short_name:',''.join(creator_short_name)
    print 'creator_personal_url:',''.join(creator_personal_url)
    print 'creator_bio_info_url:',''.join(creator_bio_info_url)
    print 'creator_full_name:',''.join(creator_full_name)
    print 'creator_buildhistory_has_built_projects_number:',creator_buildhistory_has_built_projects_number
    print 'creator_buildhistory_has_backed_projects_number:',creator_buildhistory_has_backed_projects_number
    print 'creator_friends__facebook_number:' ,''.join(creator_friends__facebook_number)
    print 'creator_Facebook_url:' ,''.join(creator_Facebook_url)
    print 'updates number:',''.join(updates)
    print 'comments_count:', comments_count




    #multi-data
    print len(rewards_level_divided_by_goal)
    print 'rewards_level_divided_by_goal:' ,retype(rewards_level_divided_by_goal)
    print 'rewards_level_name:' ,retype(rewards_level_name)
    print 'rewards_level_description:' ,retype(rewards_level_description)
    print 'rewards_backers_level_distribution:', rewards_backers_level_distribution
    print 'pledge_limit:' , pledge_limit
    #for i in range(0,len(rewards_level):
    #    print rewards_level[i]

    #print 'ship_location_info:' , ship_location_info
