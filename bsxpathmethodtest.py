
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import etree

someurl = 'https://www.kickstarter.com/projects/neliobarros/nixin-typeface?ref=discover_potd'
root_url = 'https://www.kickstarter.com'
try:
      response = Request(someurl)
      content = urllib2.urlopen(someurl).read()
      sel= etree.HTML(content)
      ##this is for some data without tab.
      req = urlopen(response)
      the_page1 = req.readlines()
except URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:


    #data_poll_url
    data_pool_url = sel.xpath('//*[@id="stats"]/div/div[3]/div/div//@data-poll_url')
    data_pool_url = ''.join(str(x) for x in data_pool_url)

    print data_pool_url
    #turn to new websites
    data_pool_url_websites = urllib2.urlopen(data_pool_url).read()
    data_pool_url_websites = ''.join(str(x) for x in data_pool_url_websites)
    a = data_pool_url_websites#.split(',')
    #print a

    def OnlyStr(s,oth=''):
       #s2 = s.lower();
       fomart = 'abcdefghijklmnopqrstuvwxyz0123456789:,'
       for c in s:
           if not c in fomart:
               s = s.replace(c,'');
       return s;
    #print(OnlyStr(a))
    name =[]
    b = OnlyStr(a).strip('project:')
    print len(b.split(','))-1
    for i in range(0,len(b.split(','))):
        name.append(b.split(',')[i].split(':'))
    dics = dict(name)
    print dics
    print 'value: %s' % dics.items()
    print 'backers_count:',  dics['backerscount']
    state = dics['state']
    print 'state:' , state
    pledged = dics ['pledged']
    print 'pledged:', pledged
    state_changed_at = dics['statechangedat']
    print 'state_changed_at:',state_changed_at
    comments_count = dics['commentscount']
    print 'comments_count:', comments_count
    id = dics['id']
    print 'id :' ,id










    #for i in range(0,len(a)):
    #    for j in range(0,len(a[i])):
    #

        #    if a[i][j] == '"':
        #        a[i].strip('"')

    #print a



    #for i in range(0,len(data_pool_url_websites)):
    #    if data_pool_url_websites[i] <> '"':
    #        data = data.append(data_pool_url_websites[i])
    #print data
    #data = ''.join(data_pool_url_websites.strip('"'))

    #print data_pool_url_websites
    #for '"' in data_pool_url_websites:

    #data = data.strip('"')
    #data = data.strip('project')



    #print data_pool_url_websites



    #creator_full_name = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[1]/span/span[2]/text()')





    #print creator_buildhistory_has_built_projects_number1
    #print creator_buildhistory_has_backed_projects_number1
    #print 'creator_buildhistory_has_backed_projects_number:', creator_buildhistory_has_backed_projects_number1







#creator_friends__facebook_number_potential =
