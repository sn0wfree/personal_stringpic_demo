import generateallurl
import opt
import time
import sys



file = open ('category1.text' , 'w')
urls = generateallurl.seekurl(1,54,200)#oringal(1,54,200)11-54

for i in xrange(0, len(urls)):
    file.write(urls[i]+'\n')
