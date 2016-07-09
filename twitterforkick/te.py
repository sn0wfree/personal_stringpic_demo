import datetime
import time


def write(file,item):
    with open(file,'w') as f:
        for i in item:
            f.write(str(i) +'\n')
def read(file):
    with open(file,'r') as f:
        f_read =f.readlines()
    return f_read

def timestamp2time(timestamp):
    date=datetime.datetime.fromtimestamp(timestamp)
    return date


a=read('/Users/sn0wfree/Dropbox/BitTorrentSync/222.txt')
print len(a)
print a[1]
clean_a=[]
for i in a:
    clean_a.append(i.split()[0])
print clean_a[1],type(clean_a[1])
stamp_a=[]
for w in clean_a:
    stamp_time_a=datetime.datetime.strptime(w, "%Y-%m-%dT%H:%M:%S")
    stamp_time_a_s=stamp_time_a.timetuple()
    stampa=time.mktime(stamp_time_a_s)
    stamp_a.append(stampa)
print len(stamp_a),len(a)
print stamp_a[1],a[1]
write('/Users/sn0wfree/Dropbox/BitTorrentSync/2222.txt',stamp_a)
print stampa,type(stamp_a)
