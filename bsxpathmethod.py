
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
    print project_name

    #projetc_ID
    for line in the_page1:
        if 'data'  in line:
            words = line.split('" ')
            for word in words:
                if 'data class="Project' in word:
                    project_ID_str = word.split('Project')[1]
        #created_at
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

    #location_id
    location_id_str = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[1]/div[2]/div[1]/div/a[1]/text()')
    location_id =''.join(location_id_str)
    project_ID = ''.join(project_ID_str)
    created_at=''.join(created_at_str)
    #state_changed_at=''.join(state_changed_at_str)
    deadline_quot=''.join(deadline_quot_str)

    print 'location_id:',location_id
    print 'project ID:', project_ID
    print 'deadline:',deadline_quot
    print 'created_at:',created_at
    #print 'state_changed_at:',state_changed_at_str



    #backers_count
    backers_count= sel.xpath('//*[@id="backers_count"]/data/text()')
    print 'backers_count:', ''.join(backers_count)

    #goal
    goal = sel.xpath('//*[@id="stats"]/div/div[2]/span/span[1]/text()')
    print 'goal:',''.join(goal)
    #pledged_amount
    pledged_amount = sel.xpath('//*[@id="pledged"]/data/text()')
    print 'pledged_amount',''.join(pledged_amount)
    #data_poll_url
    data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')

    #setup date
    #setup_date = sel.xpath('')
    #hours_left
    hours_left = sel.xpath('//*[@id="project_duration_data"]//@data-hours-remaining')
    #data-duration
    data_duration = sel.xpath('//*[@id="project_duration_data"]//@data-duration')


    #updates
    updates = sel.xpath('//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[3]/span/text()')
    print 'updates number:',''.join(updates)

    #rewardsstructure
    #rewards



    #deadline
    deadline_xpath= sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[1]/div/div/p/time/text()')
    print deadline_xpath

    #description
    description = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[1]/div[2]/p/text()')
    print 'description',''.join(description)

    #url

    #creator_info_hub
    #creator_short_name
    creator_short_name = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/h5/a/text()')
    print 'creator_short_name:',''.join(creator_short_name)


    #creator_url
    creator_personal_url = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/div[3]/div/div[2]/p/a//@href')
    print 'creator_personal_url:',''.join(creator_personal_url)
    #creator_bio_info
    creator_bio_info_shorturl_list = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/p/a[1]//@href')

    creator_bio_info_url = root_url + ''.join(str(x) for x in creator_bio_info_shorturl_list)
    print 'creator_bio_info_url:',''.join(creator_bio_info_url)

    #turn to new creator_bio_websites
    creator_bio_info = urllib2.urlopen(creator_bio_info_url).read()
    creator_bio_info_sel= etree.HTML(creator_bio_info)
    creator_full_name = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[1]/span/span[2]/text()')
    print 'creator_full_name:',''.join(creator_full_name)


    #creator_buildhistory
    creator_buildhistory_has_backed_projects_number = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[4]/a/text()')
    creator_buildhistory_has_built_projects_number = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[4]/text()')
    built_projects_number_list = creator_buildhistory_has_built_projects_number
    backed_projects_number_list = creator_buildhistory_has_backed_projects_number
    creator_buildhistory_has_built_projects_number = "".join(built_projects_number_list).strip()
    creator_buildhistory_has_backed_projects_number = "".join(backed_projects_number_list).strip()
    print 'creator_buildhistory_has_built_projects_number:',creator_buildhistory_has_built_projects_number
    print 'creator_buildhistory_has_backed_projects_number:',creator_buildhistory_has_backed_projects_number

    #facebook information
    creator_friends__facebook_number_potential = str(creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/text()'))
    if 'Not connected' in creator_friends__facebook_number_potential:
        creator_friends__facebook_number = 'Not connected'
        creator_Facebook_url = 'Not connected'
    else:
        creator_Facebook_url= creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/span[2]/a//@href')
        creator_friends__facebook_number_str = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/span[2]/a/text()')
        creator_friends__facebook_number = ''.join(creator_friends__facebook_number_str)
    print 'creator_friends__facebook_number:' ,''.join(creator_friends__facebook_number)
    print 'creator_Facebook_url:' ,''.join(creator_Facebook_url)


    data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')
    data_pool_url = ''.join(str(x) for x in data_pool_url)

    #print data_pool_url
    #turn to new websites
    data_pool_url_websites = urllib2.urlopen(data_pool_url).read()
    data_pool_url_websites = ''.join(str(x) for x in data_pool_url_websites)
    a = data_pool_url_websites#.split(',')
    #print a


    name =[]
    b = OnlyStr(a).strip('project:')
    #print len(b.split(','))-1
    for i in range(0,len(b.split(','))):
        name.append(b.split(',')[i].split(':'))
    dics = dict(name)
    #print dics
    #print 'value: %s' % dics.items()
    print 'backers_count:',  dics['backerscount']
    state = dics['state']
    print 'state:' , state
    pledged = dics ['pledged']
    print 'pledged:', pledged
    state_changed_at = dics['statechangedat']
    print 'state_changed_at:',state_changed_at
    comments_count = dics['commentscount']
    print 'comments_count:', comments_count
    id = dics['id']
    print 'id :' ,id





    #creator_Facebook_url_potential_with_connecting_facebook = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/span[2]/a//@href')










    #projetc_creator_name

    #projetc_creator_name = selector,xpath

    #projetc_creator_url




     #print soup.prettify()
