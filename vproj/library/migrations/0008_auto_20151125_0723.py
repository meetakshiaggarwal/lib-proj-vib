# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20151124_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='return_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='history',
            unique_together=set([('book_id', 'copy_id', 'member_id', 'issue_date')]),
        ),
    ]
