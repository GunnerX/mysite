# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from book.models import *
from login.models import *


class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE,  verbose_name='评论的用户', blank=True, null=True)
    chapter = models.ForeignKey(Chapter, models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
        db_table = 'comment'
        ordering = ["-c_time"]

