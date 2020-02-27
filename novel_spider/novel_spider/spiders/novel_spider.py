import scrapy
import requests
from ..items import NovelSpiderItem
class NovelSpider(scrapy.Spider):
    name = 'novelspider'
    start_urls = ['https://www.qb5.tw/']

    def parse(self, response):
        category_list = response.css('.head_t a')[2:-2]
        for category in category_list:
            category_name = category.css('a::text').extract()[0]
            category_url = category.css('a::attr(href)').extract()[0]
            meta = {
                'category_name': category_name
            }
            yield scrapy.Request(category_url, meta=meta, callback=self.get_book)

    def get_book(self, response):
        meta = response.meta
        book_list = response.css('.visitlist a')
        for book in book_list:
            book_name = book.css('a::text').extract()[0]
            book_url = book.css('a::attr(href)').extract()[0]
            meta.update({
                'book_name': book_name
            })
            yield scrapy.Request(book_url, meta=meta, callback=self.get_chapter)

    def get_chapter(self, response):
        meta = response.meta
        author = response.css('.options a::text').extract()[0][3:]
        intro = ''.join(response.css('#intro').xpath('.//text()').extract()).strip().replace('\xa0', '')
        image_url = response.css('.img_in img::attr(src)').extract()[0]

        image = requests.get(url=image_url).content
        with open('images/{}.jpg'.format(meta['book_name']), 'wb') as f:
            f.write(image)
        print(meta['book_name'],' is ok !---------')

        image = 'images/{}.jpg'.format(meta['book_name'])

        chapter_list = response.css('dd a')
        number = 0
        for chapter in chapter_list:
            number += 1
            chapter_name = chapter.css('a::text').extract()[0]
            chapter_url = chapter.css('a::attr(href)').extract()[0]
            chapter_url = 'https://www.qb5.tw' + chapter_url
            meta.update({
                'author': author,
                'intro': intro,
                'image': image,
                'chapter_name': chapter_name,
                'number': number
            })
            yield scrapy.Request(chapter_url, meta=meta, callback=self.get_content)

    def get_content(self, response):
        meta = response.meta
        content = ''.join(response.css('#content').xpath('.//text()').extract()[1:])
        meta.update({
            'content': content
        })

        item = NovelSpiderItem()
        item['category_name'] = meta['category_name']
        item['book_name'] = meta['book_name']
        item['author'] = meta['author']
        item['intro'] = meta['intro']
        item['chapter_name'] = meta['chapter_name']
        item['number'] = meta['number']
        item['content'] = meta['content']
        item['image'] = meta['image']

        return item

