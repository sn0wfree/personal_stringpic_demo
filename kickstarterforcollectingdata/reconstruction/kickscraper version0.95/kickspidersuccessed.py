#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by Lin Lu 2016
#-----------------------------------------------------------------------------------------------
'''
this code is for my dissertation.
'''
#-----------------------------------------------------------------------------------------------
###
from urllib2 import Request, urlopen, URLError
import time
import urllib2
import requests
from lxml import etree
#import funcforkick

#import MySQLdb
#import MySQLdb.cursors
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

def listleftn(l):
    lenlists =len(l)
    for i in xrange(0,lenlists):
        l[i]=l[i].strip('\n')
    return l



def webscraper_successed(someurl):
    print someurl
    root_url = 'https://www.kickstarter.com'
    try:
        someurl=str(someurl).split()
        if '?ref=category_newest' in someurl:
            aasd = someurl.rstrip("ref=category_newest")
            print aasd
            someurls= aasd.rstrip('?')+'/description'
            print someurls
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
            state=''
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            item={}
            rewards={}
            ID=0
            state=''
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
            #deadline_quot
            if 'deadline&quot;:' in line:
                words = line.split(',&quot;')
                for word in words:
                    if 'deadline' in word:
                        deadline_quot_str = word.split('&quot;:')[1]
                        #category = discover_category.rsplit('/discover/categories/')[1]
            if 'goal&quot;:' in line:
                words = line.split(',&quot;')
                for word in words:
                    if 'goal' in word:
                        goal_seek =word.split('&quot;:')[1]
        location_id_str = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/a[1]/text()')
        location_id =''.join(location_id_str).strip('\n')
        project_ID = ''.join(project_ID_str)
        created_at=''.join(created_at_str)
        category = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/a[2]/text()')
        state_changed_at=''.join(state_changed_at_str)
        deadline_quot=''.join(deadline_quot_str)
        backers_count= sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[4]/b/text()')
        goal = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div/span/text()')
        pledged_amount = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[4]/span/text()')
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
        creator_short_name = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/h5/a/text()')
        #creator_url


        #creator_bio_info
        creator_bio_info_shorturl_list = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/a//@href')
        creator_bio_info_url = root_url + ''.join(str(x) for x in creator_bio_info_shorturl_list)
        #turn to new creator_bio_websites
        creator_bio_info = urllib2.urlopen(creator_bio_info_url).read()
        creator_bio_info_sel= etree.HTML(creator_bio_info)
        creator_full_name = creator_bio_info_sel.xpath('//*[@id="main_content"]/header/div/div/div[2]/h1/a/text()')
        #creator_buildhistory
        creator_personal_url = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[1]/div[2]/ul/li/a/@href')
        ccccc=creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/text()')
        #print ccccc
        if ''.join(creator_personal_url)=='':
            creator_personal_url_s=0
        else:
            creator_personal_url_s=''.join(creator_personal_url)

        creator_buildhistory_has_built_projects_number=0
        creator_buildhistory_has_backed_projects_number=0
        for word in ccccc:
            if ' created' in word:
                #print word
                #built_projects = word
                creator_buildhistory_has_built_projects_number = word
            #else:
            #    creator_buildhistory_has_built_projects_number=0
            if 'backed' in word:
                    #creator_buildhistory_has_backed_projects_number =word.strip()
                creator_buildhistory_has_backed_projects_number=word.strip()

            #else:
            #    creator_buildhistory_has_backed_projects_number=0
        #
         #built_projects.split()

        creator_friends__facebook_number_potential_list = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[2]/text()')

        creator_friends__facebook_number_potential=str(creator_friends__facebook_number_potential_list)
        #print creator_friends__facebook_number_potential_list,creator_friends__facebook_number_potential,type(creator_friends__facebook_number_potential)
        if 'Not connected' in creator_friends__facebook_number_potential:
            creator_friends__facebook_number = 'Not connected'
            creator_Facebook_url = 'Not connected'
        else:
            creator_Facebook_url= creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[2]/span[2]/a//@href')
            creator_friends__facebook_number = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[2]/span[2]/a/text()')
            #creator_friends__facebook_number = ''.join(creator_friends__facebook_number_str)
        #print creator_Facebook_url,creator_friends__facebook_number
        data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')
        data_pool_url = ''.join(str(x) for x in data_pool_url)
        #print data_pool_url
        #turn to new websites
        #new data form
        state_other=sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/@data-project-state')

        if data_pool_url  != '':
            data_pool_url_websites = urllib2.urlopen(data_pool_url).read()
            data_pool_url_websites = ''.join(str(x) for x in data_pool_url_websites)
            a = data_pool_url_websites#.split(',')
            name =[]
            #transfor list to dictionary
            b = OnlyStr(a).strip('project:')
            for i in range(0,len(b.split(','))):
                name.append(b.split(',')[i].split(':'))
            dics = dict(name)
            #print dics
            #print 'value: %s' % dics.items()

            pledged = dics ['pledged']
            #state_changed_at = dics['statechangedat']
            comments_count = dics['commentscount']
            id = dics['id']
        else:

            pledged = 0
            #state_changed_at = ''
            comments_count = 0
            id = 0
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
        #print 'pledged', pledged
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
#someurl='https://www.kickstarter.com/projects/katherinefreer/medialounge-2015-a-pop-up-exhibition?ref=category_newest'
#(a,b,c,d)=webscraper_successed(someurl)
#print d
