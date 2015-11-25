# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='reference_id',
            field=models.ForeignKey(default=1, to='library.Member', null=True),
        ),
    ]
