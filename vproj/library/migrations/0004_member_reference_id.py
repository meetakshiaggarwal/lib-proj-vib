# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_member_reference_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='reference_id',
            field=models.ForeignKey(default=0, to='library.Member'),
        ),
    ]
