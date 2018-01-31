from scrapy import Request
from scrapy.spiders import Spider
from city_weather.items import CityWeatherItem

# 网站集合
# 需要抓取城市的网址
# ex: http://www.tianqihoubao.com/lishi/guangzhou/month/201702.html  (广州 2017年2月)
# ex: http://www.tianqihoubao.com/lishi/foshan/month/201702.html (佛山 2017年2月)
urls = [
    'http://www.tianqihoubao.com/lishi/guangzhou/month/201701.html',
    # 'http://www.tianqihoubao.com/lishi/guangzhou/month/201702.html',
    # 'http://www.tianqihoubao.com/lishi/guangzhou/month/201703.html',
    # 'http://www.tianqihoubao.com/lishi/guangzhou/month/201704.html',
]

class CityWeatherSpider(Spider):
    name = 'CityWeatherSpider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        for url in urls:
            yield Request(url, headers=self.headers)

    def parse(self, response):
        item = CityWeatherItem()
        city = response.xpath('//*[@id="bd"]/div[2]/div[6]/h3').re('<h3>(\w+)天气')[0]
        weather_records = response.xpath('//*[@id="content"]//tr')
        for record in weather_records[1:]:
            item['record_date'] = record.xpath('./td[1]/a/text()').extract()[0].strip()
            item['high_temperature'], item['low_temperature']= record.xpath('./td[3]').re('(\d+)℃\r\n')
            item['description'] = record.xpath('./td[2]').re('(\w+)</td>')[0]
            item['wind'] = record.xpath('./td[4]').re('/([\w|\S|\s]+)</td>')[0]
            item['city'] = city
            yield item
