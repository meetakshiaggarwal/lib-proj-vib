# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(default=b'default', max_length=100)),
                ('last_name', models.CharField(default=b'default', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(serialize=False, primary_key=True)),
                ('isbn_no', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('no_of_copies', models.PositiveIntegerField(default=0)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('copy_id', models.PositiveIntegerField()),
                ('availability', models.BooleanField()),
                ('ETA', models.DateField(null=True)),
                ('date_of_addition', models.DateField(auto_now_add=True)),
                ('book_id', models.ForeignKey(to='library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='CompiledBy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_id', models.ForeignKey(to='library.Author')),
                ('book_id', models.ForeignKey(to='library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='HasCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_id', models.ForeignKey(to='library.Book')),
                ('category_id', models.ForeignKey(to='library.Category')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('trans_id', models.AutoField(serialize=False, primary_key=True)),
                ('issue_date', models.DateField()),
                ('due_date', models.DateField()),
                ('return_date', models.DateField()),
                ('book_id', models.ForeignKey(to='library.Book')),
                ('copy_id', models.ForeignKey(to='library.BookCopy')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{11,13}$', message=b"Phone number must be entered in the format: '+919999999'. Up to 13 digits allowed.")])),
                ('email', models.EmailField(max_length=254)),
                ('date_of_joining', models.DateField()),
                ('reference_id', models.ForeignKey(default=1, to='library.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='member_id',
            field=models.ForeignKey(to='library.Member'),
        ),
        migrations.AddField(
            model_name='compiledby',
            name='publisher_id',
            field=models.ForeignKey(to='library.Publisher'),
        ),
        migrations.AddField(
            model_name='bookcopy',
            name='donor_id',
            field=models.ForeignKey(to='library.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='hascategory',
            unique_together=set([('book_id', 'category_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='compiledby',
            unique_together=set([('book_id', 'author_id', 'publisher_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='bookcopy',
            unique_together=set([('book_id', 'copy_id')]),
        ),
    ]
