

from urllib2 import Request, urlopen, URLError
import time
import urllib2
import requests
from lxml import etree
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

import sys



#try:
#    db = MySQLdb.connect('localhost','root','19920815','kickdatafortest');

#    cur=db.cursor()
#    cur.execute('SELECT VERSION()')
    #_conditional_insert
    #data = cur.fetchone()

    #print 'Database version :%s'%data
#except MySQLdb.Error,e:
    #print 'Error %d:%s' %(e.args[0],e.args[1])
    #sys.exit(1)

#finally:

 # pipeline dafault function
