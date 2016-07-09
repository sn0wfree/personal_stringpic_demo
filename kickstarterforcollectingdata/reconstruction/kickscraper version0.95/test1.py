


import sys

import time
import threading
import Queue

from urllib2 import Request, urlopen, URLError
import urllib2
import requests
from lxml import etree

import os


def listleftn(l):
    lenlists =len(l)
    for i in xrange(0,lenlists):
        l[i]=l[i].strip('\n')
    return l
#someurls='https://www.kickstarter.com/projects/nomiku/new-nomiku-sous-vide-wifi-connected-and-made-in-th/creator_bio'
#someurls='https://www.kickstarter.com/projects/1854224916/never-quit-smallest-powerboat-crossing-the-atlanti'
#someurls='https://www.kickstarter.com/projects/nomiku/new-nomiku-sous-vide-wifi-connected-and-made-in-th/description'
someurls='https://www.kickstarter.com/projects/223464445/project-paradigm-the-world-shift-experiment?ref=category_newest'
#someurls='https://www.kickstarter.com/projects/1807618223/dragonslayer-chapters-1-and-2?ref=category_featured'
def webscraper_failorcanceled(someurl):
    root_url = 'https://www.kickstarter.com'
    try:

            #print someurls
        response = Request(someurls)
        content = urllib2.urlopen(someurls).read()
        sel= etree.HTML(content)
          ##this is for some data without tab.
        req = urlopen(response)
        the_page1 = req.readlines()
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            item={}
            rewards={}
            ID=0
            state='Error'
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            item={}
            rewards={}
            ID=0
            state='Error'
    else:

        project_name_str = sel.xpath('//*[@id="content-wrap"]/section/div[1]/div/h2/a/text()')
        project_name = ''.join(project_name_str).strip('\n')
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
            if 'deadline&quot;:' in line:
                words = line.split(',&quot;')
                for word in words:
                    if 'deadline' in word:
                        deadline_quot_str = word.split('&quot;:')[1]
            if 'launched_at&quot;:' in line:
                words = line.split(',&quot;')
                for word in words:
                    if 'launched_at' in word:
                        launched_at_str= word.split('&quot;:')[1]
            if 'state_changed_at&quot;:' in line:
                words = line.split(',&quot;')
                for word in words:
                    if 'state_changed_at' in word:
                        state_changed_at_str= word.split('&quot;:')[1]
        #location_id
        location_id_str = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[1]/div[2]/div[1]/div/a[1]/text()')
        location_id =''.join(location_id_str).strip('\n')
        project_ID = ''.join(project_ID_str)
        launched_at=''.join(launched_at_str)
        created_at=''.join(created_at_str)
        state_changed_at=''.join(state_changed_at_str)
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

        video = sel.xpath('//*[@id="video-section"]/@data-has-video')
        #backers_count
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
        state = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/@data-project-state')[0]
        comments_count=sel.xpath('//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[4]/@data-comments-count')
        #initialation
        rewards_level_description =[]
        pledge_limit = []
        #ship_location_info
        ship_location_info = ['0']*len(rewards_level_divided_by_goal)
        #print len(rewards_level)
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
            #ship_location_info_split_list = sel.xpath(ship_location_info_a)
            #ship_location_info_split = ship_location_info_split_list
            #print ship_location_info_split, ship_location_info_split_list
            #ship_location_info_split =''.join(ship_location_info_split)
            #ship_location_info_split= str(ship_location_info_split)
            #ship_location_info[i-1] = ship_location_info_split
        deadline_xpath= sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[1]/div/div/p/time/text()')
        #project_description
        description = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[1]/div[2]/p/text()')
        #creator_info_hub
        #creator_short_name
        creator_short_name = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/h5/a/text()')
        #creator_url
        creator_personal_url = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/div[3]/div/div[2]/p/a//@href')
        #creator_bio_info
        creator_bio_info_shorturl_list = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/p/a[1]//@href')
        #                                           //*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/p/a[1]
        #                                           //*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/a
        #print creator_bio_info_shorturl_list
        #                                sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/a/@href')
        creator_bio_info_url = root_url + ''.join(creator_bio_info_shorturl_list)
        #print creator_bio_info_url
        #turn to new creator_bio_websites
        creator_bio_info = urllib2.urlopen(creator_bio_info_url).read()
        creator_bio_info_sel= etree.HTML(creator_bio_info)
        creator_full_name = creator_bio_info_sel.xpath('//*[@id="main_content"]/header/div/div/div[2]/h1/a/text()')
        #creator_buildhistory
        #print creator_full_name
        creator_personal_url = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[1]/div[2]/ul/li/a/@href')
        #print ccccc
        creator_Facebook_url=creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[*]/span[2]/a/@href')
        #
        if ''.join(creator_personal_url)=='':
            creator_personal_url_s=0
        else:
            creator_personal_url_s=''.join(creator_personal_url)

        comments_count=sel.xpath('//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[4]/@data-comments-count')

        creator_friends__facebook_number_potential_list = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]//text()')
        #print creator_friends__facebook_number_potential_list

        creator_friends__facebook_number_potential=[]
        for words in creator_friends__facebook_number_potential_list:
            if words !='\n' and words!='\n\n':
                creator_friends__facebook_number_potential.append(words)
        #print creator_friends__facebook_number_potential
        if not 'Last login' in creator_friends__facebook_number_potential[0]:
            creator_short_name=creator_friends__facebook_number_potential[0]
        else:
            creator_short_name=[]
        creator_buildhistory_has_built_projects_number='null'
        creator_buildhistory_has_backed_projects_number='null'
        creator_friends__facebook_number = 'Not connected'
        for word in creator_friends__facebook_number_potential:
            if 'created' in word:
                creator_buildhistory_has_built_projects_number=word
            if 'backed' in word:
                creator_buildhistory_has_backed_projects_number=word
        creator_friends__facebook_number_potential=str(creator_friends__facebook_number_potential_list)
        #print creator_friends__facebook_number_potential_list,creator_friends__facebook_number_potential,type(creator_friends__facebook_number_potential)

        #new data form
        #                      //*[@id="content-wrap"]/section/div[2]/div/div[2]/div[3]/div/div[5]/div/h3
                              #//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[3]/div/div[4]/div/h3
        state_other=sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[3]/div/div[*]/div/h3/text()')
        #state_other_2=sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[3]/div/div[4]/div/h3/text()')



         #                            //*[@id="content-wrap"]/section/div[2]/div/div[2]/div[3]/div/div[5]/div/p/data
        #state_changed_at_str = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[3]/div/div[*]/div/p/data/@data-value')
        #state_changed_at = ''.join(state_changed_at_str).strip('"')
        category = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[1]/div[2]/div[1]/div/a[2]/text()')

        #print state_changed_at
        deadline_date= ''.join(deadline_quot_str)
        backers_count_str = ''.join(backers_count)
        goal_str = ''.join(goal)
        pledged_amount_str =''.join(pledged_amount)
        currency_str = ''.join(currency)
        data_percent_rasied_str = ''.join(data_percent_rasied)
        hours_left_str = ''.join(hours_left)
        projectitem={}
        rewards={}

        projectitem['has_a_video']= ''.join(video)
        projectitem['project_name'] = project_name
        #projectitem[ 'project_name']= project_name
        projectitem[ 'location_ID']= location_id
        projectitem[ 'Project_ID']= project_ID
        projectitem['duration'] =''.join(data_duration)

        #print 'Project ID', id
        if state != '':
            projectitem[ 'project_state' ]= state
        else:
            projectitem[ 'project_state' ]=''.join(state_other)
        projectitem['created_at']= created_at
        projectitem['Deadline']=deadline_quot
        #print 'deadline_xpath', deadline_date
        projectitem['state_changed_at']= state_changed_at
        projectitem[ 'backers_count']= backers_count_str
        #print 'backers_count',  dics['backerscount']
        projectitem[ 'Goal']= goal_str
        projectitem[ 'pledged_amount']=pledged_amount_str
        #print 'pledged', pledged
        projectitem[ 'data_percent_rasied']= data_percent_rasied_str
        projectitem[ 'currency']= currency_str
        projectitem[ 'hours_left']= hours_left_str
        #print 'day_left', day_left
        projectitem[ 'description']=''.join(description).strip('\n')
        projectitem[ 'creator_short_name']=''.join(creator_short_name)
        projectitem[ 'creator_personal_url']=''.join(creator_personal_url)
        projectitem[ 'creator_bio_info_url']=''.join(creator_bio_info_url)
        projectitem[ 'creator_full_name']=''.join(creator_full_name)
        projectitem[ 'creator_built_projects_number']=creator_buildhistory_has_built_projects_number
        projectitem[ 'creator_buildhistory_has_backed_projects_number']=creator_buildhistory_has_backed_projects_number
        projectitem[ 'creator_friends_facebook_number' ]=''.join(creator_friends__facebook_number)
        projectitem[ 'creator_Facebook_url' ]=''.join(creator_Facebook_url)
        projectitem[ 'updates_number']=''.join(updates)
        projectitem[ 'comments_count']= comments_count
        projectitem['url']=someurl
        projectitem['launched_at']=launched_at
        #multi-data


        rewards[ 'Project_ID']= project_ID
        rewards[ 'rewards_level_divided_by_goal' ]=rewards_level_divided_by_goal
        rewards[ 'rewards_level_name' ]= listleftn(rewards_level_name)
        rewards[ 'rewards_level_description' ]=rewards_level_description
        rewards[ 'rewards_backers_level_distribution']= rewards_backers_level_distribution
        rewards[ 'pledge_limit' ]= listleftn(pledge_limit)
        projectitem['category']= ''.join(category).strip()
    return projectitem, rewards , projectitem[ 'Project_ID'] , projectitem['project_state']

def webscraper_successed(someurl,a,the_page):
    root_url = 'https://www.kickstarter.com'
    try:
        aasd = someurl.rstrip("ref=category_newest")
        someurls= aasd.rstrip('?')+'/description'
        print someurls
            #print someurls
        response = Request(someurls)
        content = urllib2.urlopen(someurls).read()
        sel= etree.HTML(content)
          ##this is for some data without tab.
        req = urlopen(response)
        the_page1 = req.readlines()
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            item={}
            rewards={}
            ID=0
            state='Error'
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            item={}
            rewards={}
            ID=0
            state='Error'
    else:
        project_name_str = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[1]/h2/span/a/text()')
        project_name = ''.join(project_name_str).strip('\n')
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
            if 'state_changed_at&quot' in line:
                words = line.split(',&quot;')
                for word in words:
                    if 'state_changed_at' in word:
                        state_changed_at_str= word.split('&quot;:')[1]
            if 'launched_at&quot;:' in line:
                words = line.split(',&quot;')
                for word in words:
                    if 'launched_at' in word:
                        launched_at_str= word.split('&quot;:')[1]
            #deadline_quot
            if 'deadline&quot;:' in line:
                words = line.split(',&quot;')
                for word in words:
                    if 'deadline' in word:
                        deadline_quot_str = word.split('&quot;:')[1]
            if '&quot;goal&quot;:' in line:
                words = line.split(',&quot;')
                for word in words:
                    if 'goal&quot;:' in word:
                        goal_seek =word.split('&quot;:')[1]
        #                            //*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/a[1]/text()

        location_id_str = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/a[1]/text()')

        print 'location is %s ' %location_id_str
        location_id =''.join(location_id_str).strip('\n')
        launched_at=''.join(launched_at_str)
        project_ID = ''.join(project_ID_str)
        created_at=''.join(created_at_str)
        category = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/a[2]/text()')
        state_changed_at=''.join(state_changed_at_str)
        deadline_quot=''.join(deadline_quot_str)
        goal=''.join(goal_seek)
        backers_count_a= sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[4]/b/text()')
        pledged_amount_a = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[4]/span/text()')
        if pledged_amount_a ==[]:
            backers_count_c=sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[5]/b/text()')

            pledged_amount_c= sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/h3/span/text()')
        else:
            backers_count_c=backers_count_a
            pledged_amount_c=pledged_amount_a
        pledged_amount = pledged_amount_c
        backers_count=backers_count_c

        data_percent_rasied = sel.xpath('//*[@id="pledged"]/@data-percent-raised')
        currency = sel.xpath('//*[@id="pledged"]/data/@data-currency')
        data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')
        video = sel.xpath('//*[@id="video-section"]/@data-has-video')
        hours_left = sel.xpath('//*[@id="project_duration_data"]//@data-hours-remaining')
        day_left = sel.xpath('//*[@id="stats"]/div/div[3]/div/div/div/text()')
        data_duration = sel.xpath('//*[@id="project_duration_data"]//@data-duration')
        updates = sel.xpath('//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[3]/span/text()')
        rewards_level_divided_by_goal = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/h2/span[1]/text()')
        rewards_level_name = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[1]/p/text()[1]')
        rewards_backers_level_distribution =sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[1]/div/ol/li[*]/div[2]/div[3]/span[@class="pledge__backer-count"]/text()')
        if data_duration == '':
            data_duration = 0
            hours_left=0
        rewards_level_description =[]
        pledge_limit = []
        #ship_location_info
        ship_location_info = ['0']*len(rewards_level_divided_by_goal)

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
        deadline_xpath= sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[1]/div/div/p/time/text()')
        #project_description
        description = sel.xpath('/html/head/meta[10]/@content')
        #creator_info_hub
        #creator_short_name
        #creator_short_name = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/h5/a/text()')
        #creator_url


        #creator_bio_info
        creator_bio_info_shorturl_list = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[*]/div[2]/div[1]/div/div[2]/div[1]/a//@href')
        #                                           //*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/a
        #print creator_bio_info_shorturl_list
        #                                sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/a/@href')
        creator_bio_info_url = root_url + ''.join(creator_bio_info_shorturl_list)
        #print creator_bio_info_url
        #turn to new creator_bio_websites
        creator_bio_info = urllib2.urlopen(creator_bio_info_url).read()
        creator_bio_info_sel= etree.HTML(creator_bio_info)
        creator_full_name = creator_bio_info_sel.xpath('//*[@id="main_content"]/header/div/div/div[2]/h1/a/text()')
        #creator_buildhistory
        #print creator_full_name
        creator_personal_url = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[1]/div[2]/ul/li/a/@href')
        #print ccccc
        creator_Facebook_url=creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[*]/span[2]/a/@href')
        #
        if ''.join(creator_personal_url)=='':
            creator_personal_url_s=0
        else:
            creator_personal_url_s=''.join(creator_personal_url)

        comments_count=sel.xpath('//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[4]/@data-comments-count')

        creator_friends__facebook_number_potential_list = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]//text()')
        #print creator_friends__facebook_number_potential_list

        creator_friends__facebook_number_potential=[]
        for words in creator_friends__facebook_number_potential_list:
            if words !='\n' and words!='\n\n':
                creator_friends__facebook_number_potential.append(words)
        #print creator_friends__facebook_number_potential
        if not 'Last login' in creator_friends__facebook_number_potential[0]:
            creator_short_name=creator_friends__facebook_number_potential[0]
        else:
            creator_short_name=[]
        creator_buildhistory_has_built_projects_number='null'
        creator_buildhistory_has_backed_projects_number='null'
        creator_friends__facebook_number = 'Not connected'
        for word in creator_friends__facebook_number_potential:
            if 'created' in word:
                creator_buildhistory_has_built_projects_number=word
            if 'backed' in word:
                creator_buildhistory_has_backed_projects_number=word
            if 'friend' in word:
                creator_friends__facebook_number= word
        creator_friends__facebook_number_potential=str(creator_friends__facebook_number_potential_list)
        #print creator_friends__facebook_number_potential_list,creator_friends__facebook_number_potential,type(creator_friends__facebook_number_potential)

        #turn to new websites
        #new data form
        state_other=sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/@data-project-state')

        #data_structure_change
        deadline_date= ''.join(deadline_xpath)
        backers_count_str = ''.join(backers_count)
        goal_str = ''.join(goal)
        pledged_amount_str =''.join(pledged_amount)
        currency_str = ''.join(currency)
        data_percent_rasied_str = ''.join(data_percent_rasied)
        hours_left_str = ''.join(hours_left)
        item = {}
        #pledged = ''
        #state_changed_at = ''
        #comments_count = ''
        #id = ''
        item['project_name'] = project_name
        #item[ 'project_name']= project_name
        item[ 'location_ID']= location_id
        item[ 'Project_ID']= project_ID
        item['duration'] =0
        item['has_a_video'] =''.join(video)
        #print 'Project ID', id
        state = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/@data-project-state')[0]

        #print 'Project ID', id
        if state != '':
            item[ 'project_state' ]= state
        else:
            item[ 'project_state' ]=''.join(state_other)


        #item[ 'project_state' ]=''.join(state_other)
        if ''.join(creator_short_name) == '':
            creator_short_name_s = 0
        else:
            creator_short_name_s = ''.join(creator_short_name)
        item['created_at']= created_at
        item['Deadline']=deadline_quot
        #print 'deadline_xpath', deadline_date
        item['state_changed_at']=state_changed_at
        item[ 'backers_count']= backers_count_str
        #print 'backers_count',  dics['backerscount']
        item[ 'Goal']= goal_seek
        item[ 'pledged_amount']=pledged_amount_str
        item[ 'data_percent_rasied']= 0
        item[ 'currency']= 0
        item[ 'hours_left']= 0
        #print 'day_left', day_left

        item[ 'description']=''.join(description).strip('\n')
        item[ 'creator_short_name']= creator_short_name_s
        item[ 'creator_personal_url']= creator_personal_url_s
        item[ 'creator_bio_info_url']=''.join(creator_bio_info_url)
        item[ 'creator_full_name']=''.join(creator_full_name).strip()
        item[ 'creator_built_projects_number']= creator_buildhistory_has_built_projects_number
        item[ 'creator_buildhistory_has_backed_projects_number']=creator_buildhistory_has_backed_projects_number
        item[ 'creator_friends_facebook_number' ]=''.join(creator_friends__facebook_number)
        item[ 'creator_Facebook_url' ]=''.join(creator_Facebook_url)
        item[ 'updates_number']=''.join(updates)
        item[ 'comments_count']= comments_count
        item['url']=someurl
        item['launched_at']=launched_at
        #multi-data
        rewards={}

        rewards[ 'Project_ID']= project_ID
        rewards[ 'rewards_level_divided_by_goal' ]=rewards_level_divided_by_goal
        rewards[ 'rewards_level_name' ]= listleftn(rewards_level_name)
        rewards[ 'rewards_level_description' ]=rewards_level_description
        rewards[ 'rewards_backers_level_distribution']= rewards_backers_level_distribution
        rewards[ 'pledge_limit' ]= listleftn(pledge_limit)
        item['category']= ''.join(category).strip('\n')
    return item, rewards , item[ 'Project_ID'] , item['project_state']



(item,rewards,id,state)=webscraper_successed(someurls,0,0)
print item['location_ID']
