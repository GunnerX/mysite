# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import pymysql
from scrapy.exceptions import DropItem

class NovelSpiderPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        database='novelsite',
        )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        self.cursor.execute('select id from book_category where categoryname = ?', (item['category_name']))
        category_id = self.cursor.fetchone()
        if not category_id:
            self.cursor.execute('insert into book_category (categoryname) values(?)', (item['category_name']))
            self.db.commit()
            self.cursor.execute('select id from book_category where categoryname = ?', (item['category_name']))
            category_id = self.cursor.fetchone()
        category_id = category_id[0]

        self.cursor.execute('select id from book_author where authoryname = ?', (item['author']))
        author_id = self.cursor.fetchone()
        if not author_id:
            self.cursor.execute('insert into book_author (authorname) values(?)', (item['author']))
            self.db.commit()
            self.cursor.execute('select id from book_author where authorname = ?', (item['author']))
            author_id = self.cursor.fetchone()
        author_id  = author_id[0]

        self.cursor.execute("SELECT id FROM books_book WHERE title = ?", (item['book_name'],))
        book_id = self.cursor.fetchone()
        if not book_id:
            self.cursor.execute('INSERT INTO book_book (title, image, intro, author_id, category_id) VALUES (?,?,?,?,?)', (item['book_name'], item['image'], item['intro'], author_id, category_id))
            self.db.commit()
            self.cursor.execute("SELECT id FROM book_book WHERE title = ?", (item['book_name'],))
            book_id = self.cursor.fetchone()
        book_id = book_id[0]

        self.cursor.execute('''INSERT INTO book_chapter (number, title, content, book_id)
                                VALUES (?,?,?,?)''',
                         (int(item['number']), item['chapter_name'], item['content'], book_id))
        self.db.commit()

        self.cursor.execute("SELECT id FROM book_book WHERE title = '{}'".format(item['book_name']))
        book_id = self.cursor.fetchone()
        if not book_id:
            self.cursor.execute('INSERT INTO book_book (title, image) VALUES ("{}", "{}")'.format(item['book_name'], 'str'))
            self.db.commit()
            self.cursor.execute("SELECT id FROM book_book WHERE title = '{}'".format(item['book_name']))
            book_id = self.cursor.fetchone()
        book_id = book_id[0]


        return item



class MyImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        print(image_paths)
        return item




