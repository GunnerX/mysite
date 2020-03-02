from django.db import models
from login.models import User

class Author(models.Model):
    author_name = models.CharField(max_length=80)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = "作者"
        db_table = 'author'
        unique_together = (('id', 'author_name'),)


class Book(models.Model):
    book_name = models.CharField(max_length=80)
    intro = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=80, blank=True, null=True)
    category = models.CharField(max_length=80, blank=True, null=True)
    author = models.CharField(max_length=80, blank=True, null=True)
    number = models.IntegerField(default=0)
    user = models.ManyToManyField(User)     # 多对多，实现收藏功能

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = "小说"
        verbose_name_plural = "小说"
        db_table = 'book'
        unique_together = (('id', 'book_name'),)


class Category(models.Model):
    category_name = models.CharField(max_length=80)

    def __str__(self):
        return self.category_name

    @classmethod
    def get_categories(cls):
        return Category.objects.all()


    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"
        db_table = 'category'
        unique_together = (('id', 'category_name'),)


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=80)
    number = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    book = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.chapter_name


    class Meta:
        verbose_name = "章节"
        verbose_name_plural = "章节"
        db_table = 'chapter'
        unique_together = (('id', 'chapter_name'),)


# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     c_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.book)
#
#     class Meta:
#         ordering = ["-c_time"]