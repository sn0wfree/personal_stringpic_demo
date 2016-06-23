import os



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

def collectfile(url):
    a=len(url)
    file = open('/Users/sn0wfree/Desktop/sorteddata/allurl.txt','w')
    for i in xrange(0,a):
        file.write(url[i]+'\n')
    file.close()
url = readfile(13)
collectfiel(url)
