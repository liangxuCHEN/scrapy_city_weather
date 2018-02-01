# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CityWeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    high_temperature = scrapy.Field()
    low_temperature = scrapy.Field()
    description = scrapy.Field()
    wind = scrapy.Field()
    record_date = scrapy.Field()
    city = scrapy.Field()


class TaobaoscrapyItem(scrapy.Item):
    pageNumber = scrapy.Field()
    itemID = scrapy.Field()
    ID = scrapy.Field()
    name = scrapy.Field()
    mainPic = scrapy.Field()
    price = scrapy.Field()
    payPerson = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    shopName = scrapy.Field()
    record_date = scrapy.Field()
    detailURL = scrapy.Field()
    categoryId = scrapy.Field()
    category = scrapy.Field()
    isTmall = scrapy.Field()
    user_id = scrapy.Field()
    market = scrapy.Field()
