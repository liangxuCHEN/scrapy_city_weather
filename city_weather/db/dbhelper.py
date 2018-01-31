# -*- coding: utf-8 -*-
from scrapy.utils.project import get_project_settings  #导入seetings配置
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis

# 初始化数据库连接:
# engine = create_engine('mysql+pymysql://root:123asd@localhost:3306/utf_sys?charset=utf8')
engine = create_engine('postgresql+psycopg2://postgres:123asd@192.168.0.186/execdb')

# 初始化redis数据库连接
Redis = redis.StrictRedis(host='localhost',port=6379,db=0)

Base = declarative_base()


class WeatherModel(Base):
    __tablename__ = 'tab_city_weather'

    id = Column(Integer, primary_key=True)
    high_temperature = Column(Integer)
    low_temperature = Column(Integer)
    description = Column(String(50))
    wind = Column(String(50))
    record_date = Column(DateTime)
    city = Column(String(20))


#创建数据表，如果数据表存在则忽视！！！
Base.metadata.create_all(engine)