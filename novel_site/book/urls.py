from django.urls import path
from .views import index, detail, chapter, category

urlpatterns = [
    path('', index, name='index'),
    path('category-<str:category_name>', category, name='category'),
    path('<int:book_id>', detail, name='detail'),
    path('<int:book_id>/<int:chapter_id>.html', chapter, name='chapter')
]
