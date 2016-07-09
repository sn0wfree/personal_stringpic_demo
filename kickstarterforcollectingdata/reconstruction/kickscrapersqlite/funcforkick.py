import threading
import Queue
import kickspider
import kickspidersuccessed
import kickspiderfail
import kickspideropt
import datetime
import time
import sys
import urllib2
import requests
from lxml import etree
import pickle
from urllib2 import Request, urlopen, URLError
import os
import unicodecsv
import csv
import pandas as pd
import numpy as np



count = 0



def index_read(file_keys,file_values):
    f_keys = open(file_keys,'r+')
    f_value=open(file_values,'r+')
    f_keys_reads=f_keys.readlines()
    f_value_reads=f_value.readlines()
    for f_keys_read in f_keys_reads:
        f_keys_r = f_keys_read.split(';')
    for f_value_read in f_value_reads:
        f_value_r = f_value_read.split(';')
    if f_keys_reads != []:
        if f_keys_r[-1] == ''  :
            f_keys_r.pop()
        if f_value_r[-1] ==''  :
            f_value_r.pop()
    else:
         f_keys_r=[]
         f_value_r=[]
    lenindex_key =  len(f_keys_r)
    index={}
    for i in xrange(0,lenindex_key):
        index[f_keys_r[i]]=f_value_r[i]
    print 'reading index completed'
    f_keys.close()
    f_value.close()
    return index


def item_read(file):
    with open(file,'r') as f:
        file=f.readlines()
        lines = file.split('')
    #for line in f:
#@profile
def projetcdata_txt_write(item,file):
    with open(file,'a+') as f:
        f.write(str(item)+';')

    #print 'saving ptoject data process completed'
#@profile
def collected_list_write(item,file):
    with open(file,'a+') as f:
        for x in item:
            f.write(str(x)+';')

#@profile
def rewardsseperategenerateprocess(rewards):
    rewards_backers_distribution_dict={}
    rewards_pledge_limit_dict={}
    rewards_pledged_amount_dict={}
    rewards_backers_distribution = rewards['rewards_backers_level_distribution']
    rewards_pledge_limit =rewards['pledge_limit']
    rewards_pledged_amount = rewards['rewards_level_divided_by_goal']
    lenrewards_backers_distribution=len(rewards_backers_distribution)
    rewards_backers_distribution_dict['Project_ID']=rewards['Project_ID']
    rewards_pledge_limit_dict['Project_ID']=rewards['Project_ID']
    rewards_pledged_amount_dict['Project_ID']=rewards['Project_ID']
    if lenrewards_backers_distribution<30:
        for i in xrange(lenrewards_backers_distribution):
            if i<len(rewards_backers_distribution):
                rewards_backers_distribution_dict['%s' %i]=rewards_backers_distribution[i]
            else:
                rewards_backers_distribution_dict['%s' %i]='0'
            if i<len(rewards_pledge_limit):
                rewards_pledge_limit_dict['%s' %i]=rewards_pledge_limit[i]
            else:
                rewards_pledge_limit_dict['%s' %i]='0'
            if i<len(rewards_pledged_amount):
                rewards_pledged_amount_dict['%s' %i]=rewards_pledged_amount[i]
            else:
                rewards_pledged_amount_dict['%s' %i]='0'
    else:
        rewards_pledged_amount_dict={}
        rewards_pledge_limit_dict={}
        rewards_backers_distribution_dict={}

def index_write(index,file_keys,file_values):
    with open(file_keys,'w') as f_keys, open(file_values,'w') as f_value:
        index_keys = list(index)
        a=len(index_keys)
        index_value=[]
        for i in xrange(0,a):
            b= index_keys[i]
            index_value.append(index[b])
        for i in xrange(0,a):
            f_keys.write(str(index_keys[i])+';')
            f_value.write(str(index_value[i])+';')
        #print 'saving process completed'


#@profile
def datagenerateprocess(url,state,sel,the_page1):
    if url != '':
        (item,rewards,id,state) = opt(url,state,sel,the_page1)
    else:
        #print 'url is empty'
        item ={}
        rewards={}
        id=0
        state='='
    #print '\ndata generate process completed'
    return item,rewards,id,state






def gcompareindexprocess(someurl):
    global new_add
    global index
    global updated
    global repeated
    try:
        response = Request(someurl)
        content = urllib2.urlopen(someurl).read()
        sel= etree.HTML(content)
        req = urlopen(response)
        the_page1 = req.readlines()
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            #a=item
            a={}
            #b=rewards
            b={}
            c=0
            d='error'
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            #a=item
            a={}
            #b=rewards
            b={}
            c=0
            d='error'
    else:
        for line in the_page1:
                #project_ID_str
            if 'data'  in line:
                words = line.split('" ')
                for word in words:
                    if 'data class="Project' in word:
                        project_ID_str = word.split('Project')[1]
        id= ''.join(project_ID_str)
        state = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/@data-project-state')[0]
    if  index.has_key(id) :
        if index[id] =='live':
            index.pop(id)
            index[id]=state
            exist_code=1
            updated+=1
            #total_item.append(item)
            #total_rewards.append(rewards)
        else:
            exist_code=0
            repeated +=1
    else:
        index[id]=state
        new_add+=1
        #total_item.append(item)
        #total_rewards.append(rewards)
        exist_code=1
    return exist_code,id,state,sel,the_page1

#@profile
def shortcompareindexprocess(someurl):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    try:
        response = Request(someurl)
        content = urllib2.urlopen(response).read()
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
        state = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/@data-project-state')[0]

        return state,sel,the_page1


#@profile
def compareindexprocess(someurl,index,new_add,updated,repeated):
    try:
        response = Request(someurl)
        content = urllib2.urlopen(someurl).read()
        sel= etree.HTML(content)
        req = urlopen(response)
        the_page1 = req.readlines()
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            #a=item
            a={}
            #b=rewards
            b={}
            c=0
            d='error'
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            #a=item
            a={}
            #b=rewards
            b={}
            c=0
            d='error'
    else:
        for line in the_page1:
                #project_ID_str
            if 'data'  in line:
                words = line.split('" ')
                for word in words:
                    if 'data class="Project' in word:
                        project_ID_str = word.split('Project')[1]
        id= ''.join(project_ID_str)
        state = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/@data-project-state')[0]
    if  index.has_key(id) :
        if index[id] =='live':
            index.pop(id)
            index[id]=state
            state=''
            exist_code=1
            updated+=1
            #total_item.append(item)
            #total_rewards.append(rewards)
        else:
            exist_code=0
            repeated +=1
    else:
        index[id]=state
        state=''
        new_add+=1
        #total_item.append(item)
        #total_rewards.append(rewards)
        exist_code=1
    return exist_code,index,new_add,updated,repeated,id,state,sel,the_page1

def opt(someurl,state,sel,the_page1):
    if state == 'live':
        (a,b,c,d)=kickspideropt.webscraper_live(someurl,sel,the_page1)
    else:
        if state == 'successful':
            (a,b,c,d) = kickspideropt.webscraper_successed(someurl,sel,the_page1)
        else:
            (a,b,c,d)= kickspideropt.webscraper_failorcanceled(someurl,sel,the_page1)
    return a,b,c,d
    #return state

def OnlyStr(s,oth=''):
   #s2 = s.lower();
   fomart = 'abcdefghijklmnopqrstuvwxyz0123456789:,'
   for c in s:
       if not c in fomart:
           s = s.replace(c,'');
   return s;

def daufcurl(someurl):
    wasd = []
    root_url = 'https://www.kickstarter.com'
    if someurl != '':
        try:
            response = Request(someurl)
            content = urllib2.urlopen(someurl).read()
            sel= etree.HTML(content)
            req = urlopen(response)
            the_page1 = req.readlines()
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
            x = sel.xpath('//*[@id="projects_list"]/div[*]/li[*]/div/div[2]/*/a/@href')
            #x2 = sel.xpath('//*[@id="projects_list"]/div[*]/li[*]/div/div[2]/div/a/@href')
            x = list(set(x))
            if x != []:
                a=len(x)
                for i in range(0,a):
                    wasd.append(root_url +x[i])
    else:
        wasd = []
    return wasd




def savingcsvforalltaskprocess(rewards,item,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount):
    total_item.append(item)
    (rewards_backers_distribution_dict,rewards_pledge_limit_dict,rewards_pledged_amount_dict)=rewardsseperategenerateprocess(rewards)
    total_rewards_backers_distribution.append(rewards_backers_distribution_dict)
    total_rewards_pledge_limit.append(rewards_pledge_limit_dict)
    total_rewards_pledged_amount.append(rewards_pledged_amount_dict)
    return total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount
    #print list(rewards)




def writeacsvprocess(file,headers,item):
    with open(file,'a') as project_data:
        project_data_csv = unicodecsv.DictWriter(project_data, headers)
        project_data_csv.writeheader()
        project_data_csv.writerows(item)
