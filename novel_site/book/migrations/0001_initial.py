# Generated by Django 2.2.10 on 2020-02-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=80)),
                ('intro', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=80, null=True)),
                ('category', models.CharField(blank=True, max_length=80, null=True)),
                ('author', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=80)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('book', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'chapter',
                'managed': False,
            },
        ),
    ]
