#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by Lin Lu 2016
#-----------------------------------------------------------------------------------------------
'''
this code is for my dissertation.
'''
#-----------------------------------------------------------------------------------------------
###
import os,time,sys,datetime

def progress_test(counts,lenfile,w):

  bar_length=30
  precent=counts/float(lenfile)
  hashes = '#' * int(precent * bar_length)
  #print counts,(float(counts)/lenfile),lenfile
  spaces = ' ' * (bar_length - len(hashes))
  sys.stdout.write("""\r%d%%|%s|read %d projects|ETA: %s """ % (precent*100,hashes + spaces,counts,w))
  #sys.stdout.flush()
  #sys.stdout.write("\rPercent: [%s] %d%%,remaining time: %.4f mins"%(hashes + spaces,counts/lenfile,w))
  sys.stdout.flush()

counts=0

    f1=time.time()

    counts+=1
    lenfile=100
    time.sleep(0.1+counts/lenfile)
    f2=time.time()
    eta=time.time()+(lenfile-counts)*(f2-f1)
    ETA=datetime.datetime.fromtimestamp(eta).time()



    progress_test(counts,lenfile,ETA)
