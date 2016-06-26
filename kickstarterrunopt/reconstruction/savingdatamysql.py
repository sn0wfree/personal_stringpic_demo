

from urllib2 import Request, urlopen, URLError
import time
import urllib2
import requests
from lxml import etree
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

import sys


class kickPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('localhost',
                db = 'kickdatafortest',
                user = 'root',
                passwd = '19920815',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = False
                )
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    # insert the data to databases
    def _conditional_insert(self, cursor, item):
        listitem = list(item)
        sql = "insert into project values(%s) "
        for x in listitem:
            cursor.execute(sql, (item[x]))
#try:
    #db = MySQLdb.connect('localhost','root','19920815','kickdatafortest');

    #cur=db.cursor()
    #cur.execute('SELECT VERSION()')
    #_conditional_insert
    #data = cur.fetchone()

    #print 'Database version :%s'%data
#except MySQLdb.Error,e:
    #print 'Error %d:%s' %(e.args[0],e.args[1])
    #sys.exit(1)

#finally:

 # pipeline dafault function
