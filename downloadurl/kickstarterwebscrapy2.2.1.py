from urllib2 import Request, urlopen, URLError
import bs4

from lxml import etree

from time import sleep
someurl = 'https://www.kickstarter.com/projects/1060627644/35000-years-in-the-making-pens-made-from-ancient-k?ref=category_featured'
req = Request(someurl)
#soup = bs4.BeautifulSoup(req.text)
#links = soup.select('div.NS_projects__header center')
root_url = 'https://www.kickstarter.com'
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
       if '<h2 class="normal mb1"><a class="' in line:
           # projetc name
           Totaltitle = line.split('">')[2]
           title = Totaltitle.split('</a></h2>')[0]

           print title
           #description
       if 'twitter:description' in line:
            description_potential = line.split('="')[2]
            description = description_potential.split('"/>')[0]
            print description
        #full-description
        #if '<div class="full-description' in line:
        #    full_description_potential = line.split('="')
        #    print full_description_potential
           #if 'T' in data_end_time_potential:
            #   data_end_time = data_end_time_potential
             #  print 'data-end_time:',data_end_time
       if '<span class="count">'  in line:
            updates_potential = line.split('">')[1]
            #.split('">')[1]
            #print updates_potential

            if '</span>' in updates_potential:
                updates = updates_potential.split('</span>')[0]
                print 'updates:', updates

       #basic info.
       if 'data'  in line:
           words = line.split('" ')
           #print words
           for word in words:
               #backers_count
               if 'data-backers-count' in word:
                   data_backers_count = word.split('"')[1]

                   print 'data_backers_count: %f' %float(data_backers_count)
               #projectID
               if 'data class="Project' in word:
                   projectID = word.split('Project')[1]
                   #print projectID
                   print 'projectID: ',projectID
               #goal
               if 'data-goal' in word:
                   data_goal = word.split('"')
                   print 'data-goal:',data_goal[1]
               if 'data-pledged' in word:
                   data_pledged = word.split('"')[1]
                   print 'data-pledged:',data_pledged
               if 'data-currency' in word:
                   data_currency = word.split('"')[1]
                   print 'data-currency:',data_currency
               if 'money usd no-code' in word:
                   goal_in_usd = word.split('">')[1]
                   print 'goal money in usd:',goal_in_usd
               if 'data-comments-count' in word:
                   data_comments_count = word.split('="')[1]
                   print 'data-comments-count:',data_comments_count
               if 'data-duration' in word:
                   data_duration_day = word.split('="')[1]
                   print 'data-duration-day:',data_duration_day
               if 'data-end_time="' in word:
                   data_end_time_potential = word.split('="')[1]
                   #print data_end_time_potential
                   if 'T' in data_end_time_potential:
                       data_end_time = data_end_time_potential
                       print 'data-end_time:',data_end_time
                           #rewardsstructure
                           
                           #rewardsstructure_level1
                           # if
                           #rewardsstructure_level1_name =




               if 'data-percent-raised' in word:
                   data_percent_raised = word.split('"')[1]
                   print 'data-percent-raised:',data_percent_raised
               # creator_name and creator_url
               if 'creator_bio">'  in word:
                   creator_name_or_url_potential = word.split('">')
                   #print creator_name_or_url_potential
                   for  creator_name_potential in creator_name_or_url_potential:
                      if 'href="' in creator_name_potential:
                          creator_personal_url = creator_name_potential.split('="')[1]
                          creator_url = root_url +creator_personal_url
                          #print creator_url
                      else:
                          if '</a></b>' in creator_name_potential:
                             creator_name = creator_name_potential.split('</a></b>')[0]
                             print creator_name

                        #print 'updates', updates
                   break

### define the fields for your item here like:
    #basic info.
    #name = scrapy.Field()
    #id = scrapy.Field()
    #desription = scrapy.Field()
    #goal = scrapy.Field()
    #url = scrapy.Field()
    #creator = scrapy.Field()
    #further info


    #backers_count = scrapy.Field()
    #pledged_amount = scrapy.Field()
    #setupdate = scrapy.Field()
    #deadline = scrapy.Field()
    #rewards = scrapy.Field()
    #rewardsstructure = scrapy.Field()
    #updated_number = scrapy.Field()
    #commits_number = scrapy.Field()
    #delivery_date = scrapy.Field()##


        #if 'twitter:text:time' in line:   # check for lines we want to find & print them
        #    days_left=line.split('"')[3]

        #if 'data-goal' in line:
        #    words = line.split(" ")             # split line into 'words'
        #    for word in words:                  # iterate through 'words'
        #        if 'data-goal' in word:
        #            target = word.split('"')    # split word at " character
                                                             # make 2nd element a float
        #            print 'target: %.4f' % float(target[1])  # then truncate to 4 d.p.
        #        if 'data-percent-raised' in word:
        #            percent = word.split('"')
        #            print 'percentage raised: %.4f  ' % (float(percent[1]) )
        #        if 'data-pledged' in word:
        #            amount_raised = word.split('"')
        #            print 'Total so far: %.4f' % float(amount_raised[1])
        #   print 'Time left: %s' % days_left
