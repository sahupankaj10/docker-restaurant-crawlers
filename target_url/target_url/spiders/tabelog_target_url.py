# -*- coding: utf-8 -*-
import re
import time
import redis
import scrapy
from math import ceil
from time import strftime
from scrapy.http.request.form import FormRequest


class TabelogTargetUrlSpider(scrapy.Spider):
    start_urls = ['https://tabelog.com']
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

    name = "tabelog_target_urls"
    redis_key_user = "tabelog_user"
    redis_key_kuchikomi = "tabelog_kuchikomi"
    redis_key_facility = "tabelog_facility"

    # analyze
    def parse(self, response):
        for sel_region in response.css('.rsttop-search__pref-container dd ul li'):
            prefecture = sel_region.css('a::attr("href")').extract_first()
            target_url = response.url + prefecture
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture)

    def parse_prefecture(self, response):
        for sel_prefecture in response.css('#tabs-panel-balloon-pref-area .list-balloon__list ul li'):
            prefecture_area = sel_prefecture.css('a::attr("href")').extract_first()
            target_url = prefecture_area
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture_sub_area)

    def parse_prefecture_sub_area(self, response):
        for sel_prefecture_area in response.css('#tabs-panel-balloon-pref-area .list-balloon__list ul li'):
            prefecture_sub_area = sel_prefecture_area.css('a::attr("href")').extract_first()
            if prefecture_sub_area is not None:
                target_url = prefecture_sub_area
                yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_prefecture_area_restaurant)

    def parse_prefecture_area_restaurant(self, response):
        total_kuchikomi = response.css('span:last-child.c-page-count__num>strong::text').extract_first()
        number_of_pages = ceil(int(total_kuchikomi) / 20)
        for page in range(1, number_of_pages + 1):
            target_url = response.url + "rstLst/{}/".format(str(page))
            yield FormRequest(target_url, method='GET', meta=response.meta, callback=self.parse_restaurant_url)

    def parse_restaurant_url(self, response):
        url_list = dict()
        count = 1
        for sel_restaurant_list in response.css('ul.rstlist-info li.list-rst'):
            restaurant_url = sel_restaurant_list.css('li.list-rst::attr("data-detail-url")').extract_first()
            restaurant_id = re.search('(?<=/)(\d+)', restaurant_url).group()

            url_json = '{"url":"' + str(restaurant_url) + '", "restaurant_id": "'+ str(restaurant_id) + '"}'
            url_json_kuchikomi = '{"url":"' + str(restaurant_url+'dtlrvwlst') + '", "restaurant_id": "'+ str(restaurant_id) + '"}'

            self.redis_db.rpush(self.redis_key_facility, url_json)
            self.redis_db.rpush(self.redis_key_kuchikomi, url_json_kuchikomi)
            self.redis_db.rpush(self.redis_key_user, url_json_kuchikomi)

            url_list[count] = url_json
            count += 1

        yield url_list
