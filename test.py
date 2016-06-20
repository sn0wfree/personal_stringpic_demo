

from scrapy.spider import Spider
from scrapy.selector import Selector

someurl = 'https://www.kickstarter.com/projects/1060627644/35000-years-in-the-making-pens-made-from-ancient-k?ref=category_featured'

#soup = bs4.BeautifulSoup(req.text)
#links = soup.select('div.NS_projects__header center')
root_url = 'http://www.kickstarter.com'
html = etree.parse(someurl)


test = html.xpath('//*[@class="pledge__title"]/text()').extract()
print test


