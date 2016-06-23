import threading
import Queue
import datetime
import generateallurl
import opt
import time
import sys
import kick

import downloadurlauto
def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue
print 'initiating collecting data'
category_urls = open ('category2.txt','r').readline()



for i in xrange(1,54):
    downloadurlauto,downloadforurl(i)
    #print 'project %d has succesful porcess and do next' % i
    time.sleep(100)
    #print '%d have succesful porcess and do next' % i
