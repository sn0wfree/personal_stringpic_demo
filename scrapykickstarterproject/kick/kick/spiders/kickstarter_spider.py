# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy.selector import Selector
from scrapy.http import  Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from bbs.items import BbsItem





class kickstarterspider(scrapy.Spiders):
    name = " kickstarter"
    allowed_domains = ["kickstarter.com"]
    start_urls = 'https://www.kickstarter.com/projects/mnbookarts/the-s-helmes-and-w-gaglione-rubber-stamp-archive?ref=category_featured'



def parse(self, response):
    sel = Selector(response)

    items = []

    for site in sel:
        item = DmozItem()
        item['name'] = site.xpath('//*[@id="content-wrap"]/section/div[1]/div/h2/a/text()').extract()
        item['creator_url'] = site.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/h5/a/text()').extract()
        item['description'] = site.xpath('//*[@id="content-wrap"]/section/div[2]/div/div[1]/div[2]/p/text()').extract()
        item.append(item)
        return item

#content-wrap > div.NS_projects__content > section.js-could-have-report-project.js-project-content.js-project-description-content.project-content > div > div > div > div > div.col.col-4 > div.mb6.mobile-hide > div > ol > li.hover-group.js-reward-available.pledge-selectable-sidebar.pledge--selected > div.pledge__info > h3
