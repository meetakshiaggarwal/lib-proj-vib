# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20151124_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaitingList',
            fields=[
                ('wait_id', models.AutoField(serialize=False, primary_key=True)),
                ('waiting_no', models.PositiveIntegerField()),
                ('book_id', models.ForeignKey(to='library.Book')),
                ('member_id', models.ForeignKey(to='library.Member')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='waitinglist',
            unique_together=set([('book_id', 'member_id', 'waiting_no')]),
        ),
    ]
