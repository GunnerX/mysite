from django.test import TestCase
from .models import *

book = '神级龙卫'
chapters = Chapter.objects.filter(book=book).order_by(int(Chapter.number))
for chapter in chapters:
    print(chapter.name, chapter.chapter_name)