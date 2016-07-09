import os

f=open('/Users/sn0wfree/BitTorrentSync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/middle60.txt','r').readlines()
#print len(f)
count =0
def createdir():
    for x in xrange(0,len(f),2000):
        locals()['url%s_num'%x] = f[x:x+2000]
        count+=1
        a =x/2000
        #print len(locals()['url%s'%x])
        os.mkdir('/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/split/url%s'%a)
        locals()['url%s'%x]=open("/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/split/url%s/url%s.txt"% (a,a),'w')
        locals()['url%scollected'%x]=open("/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/split/url%s/collected.txt"% a,'w')
        locals()['url%s1'%x]=open("/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/split/url%s/project_data.csv"% a,'w')
        locals()['url%s2'%x]=open("/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/split/url%s/rewards_pledged_amount.csv"% a,'w')
        locals()['url%s3'%x]=open("/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/split/url%s/rewards_pledge_limit.csv"% a,'w')
        locals()['url%s4'%x]=open("/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/split/url%s/rewards_backers_distribution.csv"% a,'w')
        for i in locals()['url%s_num'%x]:
            locals()['url%s'%x].write(i)
        locals()['url%s'%x].close()

def move_file_order(oldfile,newfile):
    #for
    a= "/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/split/url%s/project_data.csv"% a

    shutil.copyfile(oldfile,newfile)
    #for x in xrange(0,112):





w = os.walk("/Users/sn0wfree/BitTorrentSync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/middle60project/split")
#print w
#for (root , dirs ) in w:
#

#for (root, dirs, files) in w:
#    print len(dirs)

        #print root + '/' + name




#print count
