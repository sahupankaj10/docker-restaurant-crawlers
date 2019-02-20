# -*- coding: utf-8 -*-
import re
import time
import scrapy
from math import ceil
from time import strftime
from scrapy.exceptions import CloseSpider
from scrapy_redis.spiders import RedisSpider
from scrapy.http.request.form import FormRequest


class TabelogKuchikomiSpider(scrapy.Spider):
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
            'kuchikomi.proxy_middlewares.ProxyMiddleware': 1,
        },
    }
    COOKIES_ENABLED = True
    COOKIES_DEBUG = True
    handle_httpstatus_list = [400, 405]

    start_urls = ['https://tabelog.com/tokyo/A1307/A130701/13124391/']


    name = "tabelog_kuchikomi"
    redis_key = "tabelog_kuchikomi"
    score_type = {'Location': 'location_score', 'Sleep Quality': 'comfort_score', 'Rooms': 'room_score',
                  'Service': 'service_score', 'Value': 'price_score', 'Cleanliness': 'clean_score'}
    g_cd = ''
    d_cd = ''

    # analyze
    def parse(self, response):
        from scrapy.shell import inspect_response
        inspect_response(response, self)
    pass