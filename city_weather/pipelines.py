# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from city_weather.db.dbhelper import Redis, WeatherModel, engine
from scrapy.exceptions import DropItem
from datetime import datetime
import copy

class CityWeatherPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item


# 去重
class DuplicatesPipeline(object):
    def process_item(self, item, spider):
        key = item['city'] + item['date']
        if Redis.exists('city_date:%s' % key):
            raise DropItem("Duplicate item found: %s" % item)
        else:
            Redis.set('city_date:%s' % key,1)
            return item


# 存储到数据库
class DataBasePipeline(object):
    def open_spider(self, spider):
        self.items = []

    def process_item(self, item, spider):
        # item 用的是同一个地址，需要copy才能避免后面的修改
        item['record_date'] = datetime.strptime(item['record_date'], "%Y年%m月%d日").strftime("%Y-%m-%d %H:%M:%S")
        self.items.append(copy.deepcopy(item))

    def close_spider(self, spider):
        conn = engine.connect()
        try:
            conn.execute(WeatherModel.__table__.insert(), self.items)
        except Exception as e:
            print('插入数据出错， 错误信息：%s' % e)
        finally:
            conn.close()




# 爬取历史前n个月
class CountDropPipline(object):
    def __init__(self):
        self.count = 2

    def process_item(self, item, spider):
        if self.count == 0:
            raise DropItem("Over item found: %s" % item)
        else:
            self.count -= 1
            return item