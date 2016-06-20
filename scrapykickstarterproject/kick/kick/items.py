# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class kickstarterItem(scrapy.Item):
    # define the fields for your item here like:
    #basic info.
    name = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
    desription = scrapy.Field()
    goal = scrapy.Field()
    url = scrapy.Field()
    creator_name = scrapy.Field()
    creator_url = scrapy.Field()
    #further info
    
    
    backers_count = scrapy.Field()
    pledged_amount = scrapy.Field()
    setupdate = scrapy.Field()
    deadline = scrapy.Field()
    rewards = scrapy.Field()
    rewardsstructure = scrapy.Field()
    updated_number = scrapy.Field()
    commits_number = scrapy.Field()
    delivery_date = scrapy.Field()
    
    
    
    
    
    pass
