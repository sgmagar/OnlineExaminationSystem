# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0022_auto_20160129_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerioe',
            name='value',
        ),
        migrations.RemoveField(
            model_name='answeriom',
            name='value',
        ),
        migrations.RemoveField(
            model_name='answermoe',
            name='value',
        ),
    ]
