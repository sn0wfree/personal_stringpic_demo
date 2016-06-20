
from urllib2 import Request, urlopen, URLError
import bs4

from lxml import etree

from time import sleep
someurl = 'https://www.kickstarter.com/projects/1060627644/35000-years-in-the-making-pens-made-from-ancient-k?ref=category_featured'
req = Request(someurl)
#soup = bs4.BeautifulSoup(req.text)
#links = soup.select('div.NS_projects__header center')
root_url = 'http://www.kickstarter.com'



try:
      response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:
    the_page1 = response.readlines()      # read each line of the html file
    projecturl = someurl
    for line in the_page1:                 # iterate through the lines
       #url
       if 'twitter:description' in line:
            description_potential = line.split('="')[2]
            description = description_potential.split('"/>')[0]
            print description
            #basic info.
       if 'data'  in line:
           words = line.split('" ')
           #print words
           for word in words:
               #backers_count
               if 'data-backers-count' in word:
                   data_backers_count = word.split('"')[1]

                   print 'data_backers_count: %f' %float(data_backers_count)
                   break

                   #projectID
