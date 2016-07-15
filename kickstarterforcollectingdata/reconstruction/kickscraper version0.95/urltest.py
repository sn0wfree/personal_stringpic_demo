#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by Lin Lu 2016
#-----------------------------------------------------------------------------------------------
'''
this code is for my dissertation.
'''
#-----------------------------------------------------------------------------------------------
###

import datetime
import time


def write_n(file,item):
    with open(file,'w') as f:
        for i in item:
            f.write(str(i))
def write(file,item):
    with open(file,'w') as f:
        for i in item:
            f.write(str(i) +'\n')
def read(file):
    with open(file,'r') as f:
        f_read =f.readlines()
    return f_read

def timestamp2time(timestamp):
    date=datetime.datetime.fromtimestamp(timestamp)
    return date

b=read('/Users/sn0wfree/Dropbox/BitTorrentSync/kickstarterscrapy/kickstarterforcollectingdata/reconstruction/data/all123.text')
a=read('/Users/sn0wfree/Dropbox/BitTorrentSync/1.txt')
c=read('/Users/sn0wfree/Dropbox/BitTorrentSync/kickstarterscrapy/kickstarterforcollectingdata/reconstruction/data/allurlforkicktest.txt')
print len(b),len(list(set(b)))
print len(a), len(list(set(a)))
print len(c), len(list(set(c)))
d= list(set(c).difference(set(a)))
print len(d)
c_clean=[]
for i in c:
    c_clean.append(i.split()[0])
#print len(c),len(c_clean)
#print c[1],c_clean[1]
a_clean=[]
for i in a:
    a_clean.append(i.split()[0])
#print a[1],a_clean[1]
d_clean= list(set(c_clean).difference(set(a_clean)))
print len(d_clean)
#write('/Users/sn0wfree/Dropbox/BitTorrentSync/re.txt',d_clean)
www=read('/Users/sn0wfree/Dropbox/BitTorrentSync/re.txt')
w1=[]
w2=[]
lenwww=len(www)
for i in xrange(0,lenwww/2):
    w1.append(www[i])
for i in xrange(lenwww/2,lenwww):
    w2.append(www[i])
print len(w1),len(w2)
#write_n('/Users/sn0wfree/Dropbox/BitTorrentSync/part1.txt',w1)
#write_n('/Users/sn0wfree/Dropbox/BitTorrentSync/part2.txt',w2)
f1=read('/Users/sn0wfree/Dropbox/BitTorrentSync/part1.txt')
print f1[1]


#clean_a=[]
#for i in a:
    #clean_a.append(i.split()[0])
#print clean_a[1],type(clean_a[1])
#stamp_a=[]
#for w in clean_a:
#    stamp_time_a=datetime.datetime.strptime(w, "%Y-%m-%dT%H:%M:%S")
#    stamp_time_a_s=stamp_time_a.timetuple()
#    stampa=time.mktime(stamp_time_a_s)
#    stamp_a.append(stampa)
#print len(stamp_a),len(a)
#print stamp_a[1],a[1]
#write('/Users/sn0wfree/Dropbox/BitTorrentSync/2.txt',stamp_a)
#print stampa,type(stamp_a)
