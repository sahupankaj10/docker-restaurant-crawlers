# -*- coding: utf-8 -*-
import re
from urllib.parse import urlparse
from scrapy_redis.spiders import RedisSpider
from kuchikomi.items.tabelog_items import FacilityTabelogItem


class TabelogFacilitySpider(RedisSpider):
    name = "tabelog_facility"
    redis_key = "tabelog_facility"
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'kuchikomi.proxy_middlewares.ProxyMiddleware': 1,
        },
    }

    # analyze
    def parse(self, response):
        path = urlparse(response.url).path
        path_list = re.split('/', path)
        items = {}

        item = FacilityTabelogItem()
        item['get_url'] = response.url
        item['url_pre'] = path_list[1]
        item['url_area1'] = path_list[2]
        item['url_area2'] = path_list[3]
        item['hotel_id'] = path_list[4]

        title_list = response.css('div#location-breadcrumbs-wrap span::text').extract()
        title_list = title_list[2:]
        item['area'] = ';'.join(title_list)

        item['pillow'] = response.css('div.rdheader-rstname span.pillow-word::text').extract_first()
        item['store_name'] = self.format_list(response.css('div.rdheader-rstname span::text').extract())

        item['overall_rating'] = response.css('ul.rdheader-counts b[rel$="v:rating"] span::text').extract_first()

        for sel_data in response.css('ul.rdheader-counts '):
            item['overall_rating'] = sel_data.css("li:nth-child(1) b[rel$='v:rating'] span::text").extract_first()
            for rating_class in sel_data.css("li:nth-child(1) div.rdheader-rating__time span"):
                check_class = rating_class.css("span::attr('class')").extract_first()
                rating_value = sel_data.css("span em::text").extract_first()
                if 'dinner' in check_class:
                    item['night_total_rating'] = rating_value
                elif 'lunch' in check_class:
                    item['day_total_rating'] = rating_value

        item['number_of_reviews'] = response.css('li#rdnavi-photo span.rstdtl-navi__total-count strong::text').extract_first()
        item['number_of_photo'] = response.css('li#rdnavi-review span.rstdtl-navi__total-count em::text').extract_first()

        for sel_data in response.css('div.rdheader-info-box '):
            item['nearest_station'] = sel_data.css('.rdheader-subinfo__item--station span::text').extract_first()
            for sel_price in sel_data.css('div.rdheader-subinfo:nth-child(2)'):
                food_time_class = sel_price.css('dl:first-child div.rdheader-budget p::attr("class")').extract()
                food_time_amount = sel_price.css('dl:first-child div.rdheader-budget a.rdheader-budget__price-target::text').extract()
                for index, time_class in enumerate(food_time_class):
                    if 'dinner' in food_time_class:
                        item['night_budget'] = food_time_amount[index]
                    if 'lunch' in food_time_class:
                        item['day_budget'] = food_time_amount[index]
                regular_holiday = sel_price.css('dl:nth-child(2) dd.rdheader-subinfo__closed-text::text').get(default='null').strip()
                item['regular_holiday'] = re.sub(r'\s+', ' ', ''.join(regular_holiday))

        for sel_table in response.css('div.rstinfo-table table:nth-child(2) tr'):
            if sel_table.css('th::text').extract_first() in '受賞・選出歴':
                item['awards_selection_history'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first() in 'ジャンル':
                item['genre'] = self.format_list(sel_table.css('td span::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '予約・お問い合わせ':
                item['reservation_inquiry'] = self.format_list(sel_table.css('.rstinfo-table__tel-num::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '予約可否':
                item['reservation_acceptability'] = self.format_list(sel_table.css('.rstinfo-table__reserve-status::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '住所':
                item['street_address'] = self.format_list(sel_table.css('.rstinfo-table__address ::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '交通手段':
                item['transportation'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '営業時間':
                item['business_hours'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '支払い方法':
                item['method_of_payment'] = self.format_list(sel_table.css('td p::text').extract())

        for sel_table in response.css('div.rstinfo-table table:nth-child(4) tr'):
            if sel_table.css('th::text').extract_first().strip() in '席数':
                item['number_of_seats'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '個室':
                item['private_room'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '貸切':
                item['reserved'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '禁煙・喫煙':
                item['smoking'] = self.format_list(sel_table.css('td ::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '駐車場':
                item['parking'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '空間・設備':
                item['space_facilities'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '携帯電話':
                item['mobile'] = self.format_list(sel_table.css('td p::text').extract())

        for sel_table in response.css('div.rstinfo-table table:nth-child(6) tr'):
            if sel_table.css('th::text').extract_first().strip() in 'コース':
                 item['course'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in 'ドリンク':
                 item['drink'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '料理':
                 item['cooking'] = self.format_list(sel_table.css('td p::text').extract())

        for sel_table in response.css('div.rstinfo-table table:nth-child(8) tr'):
            if sel_table.css('th::text').extract_first().strip() in '利用シーン':
                 item['use_scene'] = self.format_list(sel_table.css('td p a::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in 'ロケーション':
                 item['location'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in 'サービス':
                 item['service'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in 'お子様連れ':
                 item['children'] = self.format_list(sel_table.css('td p::text').extract_first())
            elif sel_table.css('th::text').extract_first().strip() in 'ホームページ':
                 item['home_page'] = self.format_list(sel_table.css('td a span::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '公式アカウント':
                 item['official_account'] = self.format_list(sel_table.css('td a span::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in 'オープン日':
                 item['open_date'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '電話番号':
                 item['phone_number'] = self.format_list(sel_table.css('td p strong::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '備考':
                 item['remarks'] = self.format_list(sel_table.css('td p::text').extract())
            elif sel_table.css('th::text').extract_first().strip() in '初投稿者':
                item['original_contributor'] = self.format_list(sel_table.css('td p span::text').extract())

        items[1] = item
        yield items

    @staticmethod
    def format_list(text_list):
        formatted_text = re.sub(r'\s+', '', ''.join(text_list))
        return formatted_text if formatted_text is not None else 'null'
