def readfile():

    for i in xrange(1,file):
        locals()['file'+str(i)]=open(file ,'r').readlines()
        print type(locals()['file'+str(i)])
        url = url + (locals()['file'+str(i)])
        locals()['file'+str(i)].close()

    url = list(set(url))
    return url

def collectfile(url,file):
    a=len(url)
    file = open(file,'a+')
    for i in xrange(0,a):
        file.write(url[i]+'\n')
    file.close()

file_unclear_file = open('data/allurlforkicktest.txt','r')
file =file_unclear_file.readlines()
lenfile = len(file)

urlT20=[]
url80=[]
top20project='data/top20project.txt'
last80project='data/last80project.txt'
for i in xrange(0,lenfile/20):
    someurl =file[i].strip()
    urlT20.append(someurl)

for j in xrange(lenfile/20,lenfile):
    someurl =file[i].strip()
    url80.append(someurl)
collectfile(url80,last80project)
collectfile(urlT20,top20project)

#print file_unclear
print len(file)
