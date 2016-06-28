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

def read_url_file(file):
    with open (file,'r') as file_unclear_file:
        file_unclear = []
        file_unclear_list =file_unclear_file.readlines()
        #for x in file_unclear_list:
            #print x

            #print x
            #file_unclear.appen(x)
        return file_unclear_list
def projetcdata_txt_write(item,file):
    f= open(file,'a')
    lenitem=len(item)
    if lenitem>1:
        for i in xrange(0,lenitem):
            f.write(item[i])
    f.close()

def projetcdata_txt_wholewrite(item,file):
    f= open(file,'a')
    f.write(str(item))
    f.close()




    #print 'saving ptoject data process completed'
def collected_list_overwrite(item,file):
    f = open (file,'w')
    lenitem=len(item)
    for i in xrange(0,lenitem):
        f.write(item[i])
    f.close()

def writeafile(x,file):
    f=open(file,'a+')
    clean_list = list(set(x))
    global count
    hashes = '#' * int(count)
    lenallurl_clean_list = len(clean_list)
    for i in xrange(0, lenallurl_clean_list):
        if clean_list[i] != '':
            #print clean_list[i]
            f.write(clean_list[i])
            sys.stdout.write("\rthis spider has already written %d urls/project" % count)
            count = count + 1
            sys.stdout.flush()

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
def index_write(index,file_keys,file_values):
    f_keys= open(file_keys,'w')
    f_value = open(file_values,'w')
    index_keys = list(index)
    a=len(index_keys)
    index_value=[]
    for i in xrange(0,a):
        b= index_keys[i]
        index_value.append(index[b])
    for i in xrange(0,a):
        f_keys.write(str(index_keys[i])+';')
        f_value.write(str(index_value[i])+';')
    f_keys.close()
    f_value.close()
    #print 'saving process completed'

def item_read(file):
    with open(file) as f:
        file=f.readlines()
        lines = file.split('')
    #for line in f:
def readfile():
    for i in xrange(1,x):
        locals()['file'+str(i)]=open('/Users/sn0wfree/Desktop/categorydata/url%s.text' %i ,'r').readlines()
        print type(locals()['file'+str(i)])
        url = url + (locals()['file'+str(i)])
        locals()['file'+str(i)].close()
    url = list(set(url))
    return url

    #print type(url)
    #print 'ok'
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
    if lenrewards_backers_distribution<50:
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


    return rewards_backers_distribution_dict,rewards_pledge_limit_dict,rewards_pledged_amount_dict


#@profile
def datagenerateprocess(url,state,sel,the_page1):
    someurl=''.join(url.split())
    if state != 'Error':
        if state == 'live':

            (item,rewards,ID,state)=kickspideropt.webscraper_live(someurl,sel,the_page1)
        else:
            if state == 'successful':
                (item,rewards,ID,state) = kickspideropt.webscraper_successed(someurl,sel,the_page1)
            else:
                (item,rewards,ID,state)= kickspideropt.webscraper_failorcanceled(someurl,sel,the_page1)
    else:
        #print 'url is empty'
        item ={}
        rewards={}
        ID=0
        state='Error'
    return item,rewards,ID,state

#@profile
def compareindexprocess(url):
    someurl =''.join(url.split())
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
            state='Error'
            exist_code=0
            ID=0
            sel=0
            the_page1=0

        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            state='Error'
            exist_code=0
            ID=0
            sel=0
            the_page1=0
    else:
        for line in the_page1:
                #project_ID_str
            if 'data'  in line:
                words = line.split('" ')
                for word in words:
                    if 'data class="Project' in word:
                        project_ID_str = word.split('Project')[1]
        ID= ''.join(project_ID_str)
        state = sel.xpath('//*[@id="content-wrap"]/div[2]/section[1]/@data-project-state')[0]

    return ID,state,sel,the_page1

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



#@profile
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




def discorurl(y):
    x = daufcurl(y)
    someurl = []
    if x != []:
        someurl = x
    return someurl
