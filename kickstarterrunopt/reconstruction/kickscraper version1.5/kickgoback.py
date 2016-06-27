import funcforkick
import kickspider
import downloadurl
import threading
import Queue
import datetime
import time
import sys






db = MySQLdb.connect('localhost','root','19920815','kickdatafortest');

cur=db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS \
        Project (Project_ID INT PRIMARY KEY NOT NULL,
                 project_name VARCHAR(100) NOT NULL,
                 location_ID VARCHAR(30) NOT NULL,
                 duration INT,
                 has_a_video VARCHAR(10),
                 project_state VARCHAR(10),
                 created_at INT,
                 Deadline INT,
                 state_changed_at VARCHAR(30),
                 backers_count VARCHAR(30),
                 Goal VARCHAR(30),
                 pledged_amount VARCHAR(30),
                 data_percent_rasied VARCHAR(5),
                 currency VARCHAR(10),
                 hours_left VARCHAR(30),
                 description VARCHAR(100),
                 creator_short_name VARCHAR(30),
                 creator_personal_url VARCHAR(1000),
                 creator_bio_info_url VARCHAR(100),
                 creator_full_name VARCHAR(30),
                 creator_buildhistory_has_built_projects_number VARCHAR(20),
                 creator_buildhistory_has_backed_projects_number VARCHAR(20),
                 creator_friends__facebook_number VARCHAR(20),
                 creator_Facebook_url VARCHAR(20),
                 updates_number VARCHAR(20),
                 comments_count VARCHAR(1000),
                 category VARCHAR(30),
                 )")





def conditional_insert(cursor, item):
    listitem = list(item)
    sql = "insert into  (%s)\ values('%s') "
    for x in listitem:
        cursor.execute(sql, (x,item[x]))









def index_read(file_keys,file_values):
    f_keys=open(file_keys,'r')
    f_value=open(file_values,'r')

    f_keys_reads=f_keys.readlines()
    f_value_reads=f_value.readlines()
    for f_keys_read in f_keys_reads:
        f_keys_r = f_keys_read.split(';')
    for f_value_read in f_value_reads:
        f_value_r = f_value_read.split(';')


    if f_keys_r[-1] == ''   :
        f_keys_r.pop()
    if f_value_r[-1] ==''  :
        f_value_r.pop()
    lenindex_key =  len(f_keys_r)
    index={}
    for i in xrange(0,lenindex_key):
        index[f_keys_r[i]]=f_value_r[i]
    f_keys.close()
    f_value.close()
    print 'reading index completed'
    return index


def index_write(index,file_keys,file_values):
    f_keys=open(file_keys,'w')
    f_value=open(file_values,'w')
    index_keys = list(index)
    a=len(index_keys)
    index_value=[]
    for i in xrange(0,a):
        b= index_keys[i]
        index_value.append(index[b])
    for i in xrange(0,a):
        f_keys.write(str(index_keys[i])+';')
        f_value.write(str(index_value[i])+';')
    f_keys.close()
    f_value.close()
    print 'saving process completed'



def extend_result(x,y,a,b):
    a.extend(x)
    b.extend(y)
    return a,b


def compareindexprocess(id,state,index):
    a=1
    if id != 0:
        if  index.has_key(id) :
            if index[id] =='live':
                index.pop(id)
                index[id]=state
                a=1
            else:
                a = 0
                #a=['replicated projetcs']
        else:
            #a=['replicated projetcs']
            a = 1
            index[id]=state
    else:
        a = 0
    return index, a

def datagenerateprocess(url):
    if url != '':
        (item,rewards,id,state) = kickspider.kickgowebscraper(url)
    else:
        #print 'url is empty'
        (item,rewards,id,state) =(0,0,0,0)
    print 'data generate process completed'
    return item,rewards,id,state
#construct opt index dic for list
##read original index
#f = 'index.csv'
#f_items = 'data.csv'
#f_rewards = 'rewards.csv'
#index =csv_reader(f)

start = time.time()
count = 0
global index
global total_item
global total_rewards
print 'begin to creat index file'
#index = index_read(file_keys,file_values)
print 'begin to scrap'






#total_item_lines = open ('data.txt','r').readlines()
#total_rewards_lines= open ('rewards.txt','r').readlines()
#index = {}
total_item=[]
total_rewards=[]




#a=1 means 'replicated projetcs'



#read projetc urls
print 'begin reading urls file'
file_unclear = open('allurlforkicktest.txt',r),readlines()
print 'reading list completed'
file =list(set(file_unclear))
#lenfile200 = len(file)/200
#lenfile = len(file)

queue = Queue.Queue()
class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while 1:
            target = self.queue.get()
            print 'begin collecting data'
            (item,rewards,id,state)= datagenerateprocess(target)
            (index,exist_code) = compareindexprocess(id,state,index)
            if exist_code == 1:
                total_item_part.append(item)
                total_rewards_part.append(rewards)

            #x = discorurl(target)
            #file = open('allurlforkicktest.txt','a')
            #writeafile(x,file)
            #time.sleep(1/10)
            self.queue.task_done()
def main(url,core):
    a = len(url)
    for j in xrange(core):
        t = ThreadClass(queue)
        t.setDaemon(True)
        t.start()
    for i in range(0,a):
        queue.put(url[i])
    queue.join()

print 'reading urls file completed'
print 'begin to collecting data'
total_item_part=[]
total_rewards_part=[]
def decomposition(x):
    for i in xrange(1,lenfile200+1):
        if lenfile200 >1:
            if i < lenfile200 :
                for j in xrange((i-1)*200,i*200):
                    locals()['urls%s' %i].append(file[j])
            else:
                for j in xrange ((lenfile200-1)*200,lenfile):
                    locals()['urls%s' % lenfile200].append(file[j])
        else:
            for j in xrange(0,lenfile):
                urls1.append(file[j])

    #main(file,1)
    a = len(urls)
    for i in range(0,a):
        (item,rewards,id,state)= datagenerateprocess(file[i])
        (index,exist_code) = compareindexprocess(id,state,index)
        if exist_code == 1:
            total_item_part.append(item)
            total_rewards_part.append(rewards)



    (total_item,total_rewards)= extend_result(total_item_part,total_rewards_part,total_item,total_rewards)
    timesleep(1)
    sys.stdout.write("\rthis spider has already written %d *200 urls/project" % count)

#csv_writer(index,f,w)
#index_write(index,file_keys,file_values)
#csv_writer(total_item,f_items,a)
#csv_writer(total_rewards,f_rewards,a)
end = time.time()
print end-start
