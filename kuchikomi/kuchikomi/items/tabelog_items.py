# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserTabelogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hotel_id            = scrapy.Field()
    kuchikomi_id        = scrapy.Field()
    customer_id         = scrapy.Field()
    customer_name       = scrapy.Field()
    number_of_visit     = scrapy.Field()
    get_url             = scrapy.Field()
    night_total_rating      = scrapy.Field()
    night_culinary_rating   = scrapy.Field()
    night_service_rating    = scrapy.Field()
    night_atmosphere_rating = scrapy.Field()
    night_cp_rating         = scrapy.Field()
    night_drink_rating      = scrapy.Field()
    night_amount            = scrapy.Field()
    day_total_rating        = scrapy.Field()
    day_culinary_rating     = scrapy.Field()
    day_service_rating      = scrapy.Field()
    day_atmosphere_rating   = scrapy.Field()
    day_cp_rating           = scrapy.Field()
    day_drink_rating        = scrapy.Field()
    day_amount              = scrapy.Field()

class KuchikomiTabelogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hotel_id            = scrapy.Field()
    kuchikomi_id        = scrapy.Field()
    customer_id         = scrapy.Field()
    customer_name       = scrapy.Field()
    number_of_visit     = scrapy.Field()
    get_url             = scrapy.Field()
    night_total_rating      = scrapy.Field()
    night_culinary_rating   = scrapy.Field()
    night_service_rating    = scrapy.Field()
    night_atmosphere_rating = scrapy.Field()
    night_cp_rating         = scrapy.Field()
    night_drink_rating      = scrapy.Field()
    night_amount            = scrapy.Field()
    day_total_rating        = scrapy.Field()
    day_culinary_rating     = scrapy.Field()
    day_service_rating      = scrapy.Field()
    day_atmosphere_rating   = scrapy.Field()
    day_cp_rating           = scrapy.Field()
    day_drink_rating        = scrapy.Field()
    day_amount              = scrapy.Field()