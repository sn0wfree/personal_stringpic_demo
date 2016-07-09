def re(file):
    with open(file,'r') as f:
        f_collected_str=f.readlines()
        f_collected=[]
        for url in f_collected_str:
            f_collected.append(''.join(url.split()))

    return f_collected

def wr(file,item):
    with open(file,'w') as f:
        for url in item:
            f.write(url+'\n')


a=re('/Users/sn0wfree/Dropbox/BitTorrentSync/collected.txt')
#a=list(set(a))
c=re('/Users/sn0wfree/Dropbox/BitTorrentSync/kickstarterscrapy/kickstarterforcollectingdata/reconstruction/data/all123.text')
c=list(set(c))
d =list(set(c).difference(set(a)))
print len(a),len(c),len(d)
print a[1]
print c[1]
lend=len(d)
d1=[]
d2=[]
for i in xrange(0,lend/2):
    d1.append(d[i])
for i in xrange(lend/2,lend):
    d2.append(d[i])
print len(d1),len(d2)
wr('/Users/sn0wfree/Desktop/d1.txt',d1)
wr('/Users/sn0wfree/Desktop/d2.txt',d2)
