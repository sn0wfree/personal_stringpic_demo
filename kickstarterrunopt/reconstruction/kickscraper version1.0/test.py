import csv
import kickspider
import sys
import funcforkick
import time
import pandas as pd
import numpy as np
import multiprocessing as mp


list = open('data/last80project.txt','r+').readlines()
list_clean =list(set(list))

lenlist =len(list_clean)

















#def job(x):
#    cd=x/2
#    s=cd/10
#    d=s/100
#    return d,s,cd

#def multicore():
#    pool =mp.Pool()
#    (d,s,cd) = pool.map_async(job,range(00000000))




#if __name__=='__main__':
#    start = time.time()
#    multicore()
#    end = time.time()
#    print end-start
