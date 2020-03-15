# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelSpiderItem(scrapy.Item):
    category_name = scrapy.Field()
    book_name = scrapy.Field()
    author = scrapy.Field()
    intro = scrapy.Field()
    chapter_name = scrapy.Field()
    number = scrapy.Field()
    content = scrapy.Field()

    image_urls = scrapy.Field()
    images  =scrapy.Field()

