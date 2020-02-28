from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *

# 小说列表页
def detail(request, category_name=None):
    if category_name:
        category = Category.objects.get(category_name=category_name)
        books = Book.objects.filter(category=category_name)
    else:
        category = None
        books = Book.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    context = {
        'books': books,
        'category': category,
        'categories': categories,
    }
    return render(request, 'detail.html', context)


# 小说详情页
def novel(request, book_id):
    book = Book.objects.get(pk=book_id)
    categories = Category.objects.all()
    chapters = Chapter.objects.filter(book=book.book_name).order_by('number')
    context = {
        'book': book,
        'chapters': chapters,
        'categories': categories,
    }
    return render(request, 'novel.html', context)

# 章节页
def chapter(requests, book_id, chapter_id):
    book = Book.objects.get(pk=book_id)
    chapters = Chapter.objects.filter(book=book.book_name).order_by('number')
    chapter = chapters.get(pk=chapter_id)
    try:
        prev_chapter = chapters.get(number=(chapter.number-1))
    except Chapter.DoesNotExist:
        prev_chapter = None
    try:
        next_chapter = chapters.get(number=(chapter.number+1))
    except Chapter.DoesNotExist:
        next_chapter = None

    categories = Category.objects.all()
    context = {
        'book': book,
        'chapter': chapter,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter,
        'categories': categories
    }
    return render(requests, 'chapter.html', context)



