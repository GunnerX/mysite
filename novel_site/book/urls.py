from django.urls import path
from .views import  detail, chapter, novel

urlpatterns = [
    path('', detail, name='detail'),
    path('category-<str:category_name>', detail, name='detail'),
    path('<int:book_id>', novel, name='novel'),
    path('<int:book_id>/<int:chapter_id>.html', chapter, name='chapter')
]

