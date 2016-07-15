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

def progress_test():
  bar_length=30
  for percent in xrange(0, 100):
    hashes = '#' * int(percent/100.0 * bar_length)
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent: [%s] %d%%"%(hashes + spaces, percent))
    sys.stdout.flush()
    time.sleep(1)


if __name__-'__main__':
    for i in xrange(1,54):
        print 'initiating collecting data'
        downloadurlauto.downloadforurl(i)
        #print 'project %d has succesful porcess and do next' % i
        #progress_test()
        #print '%d have succesful porcess and do next' % i
