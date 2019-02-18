# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from crawlers.items import CrawlersItem
import re


class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    allowed_domains = ['rozetka.com.ua']
    start_urls = ['https://rozetka.com.ua/notebooks/c80004/filter/producer=apple/']

    def parse(self, response):
        products = response.xpath('//div[@data-view_type="catalog_with_hover"]')
        for product in products:
            img = product.xpath('div//img/@src').extract_first()
            name = product.xpath('div//img/@alt').extract_first()
            price = product.xpath('div//script/text()').extract_first()
            price = urllib.parse.unquote(price)
            price = re.search('price\":\d*', price).group(0)
            price = int(price.replace('price":', ''))
            item = CrawlersItem({'name': name,
                                 'price': price,
                                 'image_urls': [img]})
            yield item

