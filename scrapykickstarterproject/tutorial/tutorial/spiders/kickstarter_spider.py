# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

class kickstarterspider(scrapy.Spiders):
    name = " kickstarter"
    allowed_domains = ["kickstarter.com"]
    start_urls = 'https://www.kickstarter.com/projects/mnbookarts/the-s-helmes-and-w-gaglione-rubber-stamp-archive?ref=category_featured'



def parse(self, response):
  for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc
