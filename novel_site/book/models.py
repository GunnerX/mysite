# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=80)

    def __str__(self):
        return self.author_name

    class Meta:
        managed = False
        db_table = 'author'
        unique_together = (('id', 'author_name'),)


class Book(models.Model):
    book_name = models.CharField(max_length=80)
    intro = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=80, blank=True, null=True)
    category = models.CharField(max_length=80, blank=True, null=True)
    author = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.book_name

    class Meta:
        managed = False
        db_table = 'book'
        unique_together = (('id', 'book_name'),)


class Category(models.Model):
    category_name = models.CharField(max_length=80)

    def __str__(self):
        return self.category_name

    class Meta:
        managed = False
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
        managed = False
        db_table = 'chapter'
        unique_together = (('id', 'chapter_name'),)
