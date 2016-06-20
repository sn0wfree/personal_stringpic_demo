
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import etree

someurl = 'https://www.kickstarter.com/projects/1060627644/35000-years-in-the-making-pens-made-from-ancient-k?ref=category_featured'
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

    #project_name
    project_name = sel.xpath('//*[@id="content-wrap"]/section/div[1]/div/h2/a/text()')
    print project_name

    #projetc_ID
    for line in the_page1:
        if 'data'  in line:
            words = line.split('" ')
            for word in words:
                if 'data class="Project' in word:
                    project_ID = word.split('Project')[1]
                    #print projectID
                    print 'project ID: ',project_ID
                    #projetc_ID = selector.xpath()

    #backers_count
    backers_count= sel.xpath('//*[@id="backers_count"]/data/text()')
    print backers_count

    #goal
    goal = sel.xpath('//*[@id="stats"]/div/div[2]/span/span[1]/text()')
    print goal

    #description
    description = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[1]/div[2]/p/text()')
    print description

    #url

    #creator_info_hub
    #creator_short_name
    creator_short_name = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/h5/a/text()')
    print creator_short_name
    #creator_url
    creator_personal_url = sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/div[3]/div/div[2]/p/a//@href')
    print creator_personal_url
    #creator_bio_info
    creator_bio_info_shorturl =sel.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/p/a[1]//@href')
    creator_bio_info_url = root_url +creator_bio_info_shorturl

    creator_bio_info = urllib2.urlopen(creator_bio_info_url).read()
    creator_bio_info_sel= etree.HTML(creator_bio_info)
    creator_full_name = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[1]/span/span[2]/text()')
    print creator_full_name

    #creator_bulidhistory
    creator_bulidhistory_has_bulit_projetcs_number = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[4]/a/text()')
    creator_bulidhistory_has_backed_projetcs_number = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[4]/text()')
    print creator_bulidhistory_has_bulit_projetcs_number, creator_bulidhistory_has_backed_projetcs_number

    #creator_friends__facebook_number_potential = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/text()').extract()
    #if 'Not connected' in creator_friends__facebook_number_potential:
    #    creator_friends__facebook = 'Not connected'

    #creator_Facebook_url_potential= creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/span//@class').extract()
    #creator_friends__facebook_number_potential_with_connecting_facebook = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/span[2]/a/text()').extract()
    #creator_Facebook_url_potential_with_connecting_facebook = creator_bio_info_sel.xpath('//*[@id="bio"]/div/div[2]/div[3]/span[2]/a//@href').extract()










    #projetc_creator_name

    #projetc_creator_name = selector,xpath

    #projetc_creator_url




     #print soup.prettify()
