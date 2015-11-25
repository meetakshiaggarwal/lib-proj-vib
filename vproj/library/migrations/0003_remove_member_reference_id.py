# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20151106_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='reference_id',
        ),
    ]
