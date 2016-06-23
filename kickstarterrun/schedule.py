import threading
import Queue
import datetime
import generateallurl
import opt
import time
import sys

import downloadurlauto
def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue
for i in (1,54):
    print 'initiating collecting data'
    try:
        file = open ('category1.text','r')
         #downloadurlauto.downloadforurl(i)
    except BaseException as e:
        print(str(e))
        break
    else:
        pass
    print 'project %d has succesful porcess and do next' % i
    time.sleep(100)
    #print '%d have succesful porcess and do next' % i
