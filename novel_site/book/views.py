from django.shortcuts import render
from .models import *

# 根目录
def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context)

# 图书详情页
def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    chapters = Chapter.objects.filter(book=book.book_name).order_by('number')
    context = {
        'book': book,
        'chapters': chapters
    }
    return render(request, 'detail.html', context)

# 章节页
def chapter(requests, book_id, chapter_id):
    book = Book.objects.get(pk=book_id)
    chapter = Chapter.objects.filter(book=book.book_name).get(pk=chapter_id)
    context = {
        'book': book,
        'chapter': chapter,
    }
    return render(requests, 'chapter.html', context)