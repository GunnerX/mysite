from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
from comment.models import Comment

# 小说,分类列表页
def detail(request, category_name=None):
    all_books = Book.objects.all()
    hot_books = all_books.order_by('-number')[:10]
    if category_name:   # 分类列表页
        category = Category.objects.get(category_name=category_name)
        books = all_books.filter(category=category_name).order_by('-number')
    else:               # 首页列表页
        category = None
        books = all_books.order_by('?')[:20]        # 随机获得10本书 有问题 遍历了一遍表


    paginator = Paginator(books, 10)    # 分页逻辑
    page = request.GET.get('page')
    books = paginator.get_page(page)
    context = {
        'books': books,
        'hot_books': hot_books,
        'category': category,
        'categories': Category.get_categories(),
    }
    return render(request, 'detail.html', context)


# 用户个人空间
def user_space(request, user_id):
    user = User.objects.get(pk=user_id)
    books = user.book_set.all()
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    context = {
        'books': books,
        'categories': Category.get_categories(),
    }
    return render(request, 'detail.html', context)

# 小说详情页
def novel(request, book_id):
    book = Book.objects.get(pk=book_id)
    chapters = Chapter.objects.filter(book=book.book_name).order_by('number')
    is_fav = False       # 当前登录用户是否收藏了当前小说
    if request.session.get('is_login', None):   # 如果登录了
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        book = Book.objects.get(pk=book_id)
        is_fav = True
        try:
            user.book_set.get(pk=book_id)
        except Book.DoesNotExist:
            is_fav = False

    context = {
        'book': book,
        'chapters': chapters,
        'categories': Category.get_categories(),
        'is_fav': is_fav
    }
    return render(request, 'novel.html', context)

# 添加收藏
def add_fav(request, book_id):
    if not request.session.get('is_login', None):
        return redirect('http://127.0.0.1:8000/books/'+str(book_id))
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    book = Book.objects.get(pk=book_id)
    book.user.add(user)

    book.number += 1
    book.save()
    return redirect('http://127.0.0.1:8000/books/'+str(book_id))

# 取消收藏
def del_fav(request, book_id):
    if not request.session.get('is_login', None):
        return redirect('books/' + str(book_id))
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    book = Book.objects.get(pk=book_id)
    book.user.remove(user)

    book.number -= 1
    book.save()
    return redirect('http://127.0.0.1:8000/books/' + str(book_id))


# 章节页
def chapter(request, book_id, chapter_id):
    book = Book.objects.get(pk=book_id)
    chapters = Chapter.objects.filter(book=book.book_name).order_by('number')
    chapter = chapters.get(pk=chapter_id)
    comments = chapter.comment_set.all().order_by('c_time')
    try:
        prev_chapter = chapters.get(number=(chapter.number-1))  # 上一章下一章
    except Chapter.DoesNotExist:
        prev_chapter = None
    try:
        next_chapter = chapters.get(number=(chapter.number+1))
    except Chapter.DoesNotExist:
        next_chapter = None

    context = {
        'book': book,
        'chapter': chapter,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter,
        'categories': Category.get_categories(),
        'comments': comments,
    }
    return render(request, 'chapter.html', context)


# 添加评论
def add_comment(request, book_id, chapter_id):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        chapter = Chapter.objects.get(pk=chapter_id)
        comment_content = request.POST.get('comment')
        comment = Comment(content=comment_content)
        comment.user = user
        comment.chapter = chapter
        comment.save()
    return redirect('/books/{}/{}.html'.format(book_id, chapter_id))

def search(request):
    all_books = Book.objects.all()
    hot_books = all_books.order_by('-number')[:10]
    if request.method == 'GET':
        world = request.GET.get('world')
        books = Book.objects.filter(book_name__icontains=world)
        context = {
            'books': books,
            'hot_books': hot_books,
            'categories': Category.get_categories(),
        }
    return render(request, 'search.html', context)

def about(request):
    return render(request, 'about.html')

