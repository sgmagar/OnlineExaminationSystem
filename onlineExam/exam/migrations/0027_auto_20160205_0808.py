# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0026_auto_20160205_0755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news',
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.URLField(default=None),
        ),
    ]
