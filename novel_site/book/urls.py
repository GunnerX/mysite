from django.urls import path
from .views import  *

urlpatterns = [
    path('', detail, name='detail'),
    path('category/<str:category_name>', detail, name='detail'),
    path('<int:book_id>', novel, name='novel'),
    path('<int:book_id>/<int:chapter_id>.html', chapter, name='chapter'),
    path('add/<int:book_id>', add_fav, name='add_fav'),
    path('delete/<int:book_id>', del_fav, name='del_fav'),
    path('add_comment/<int:book_id>/<int:chapter_id>', add_comment, name='add_comment'),
    path('search', search, name='search')
]

