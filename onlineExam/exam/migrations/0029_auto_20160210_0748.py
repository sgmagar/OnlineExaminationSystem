# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0028_auto_20160209_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerioe',
            name='hint',
        ),
        migrations.RemoveField(
            model_name='answeriom',
            name='hint',
        ),
        migrations.RemoveField(
            model_name='answermoe',
            name='hint',
        ),
        migrations.AddField(
            model_name='questionioe',
            name='hint',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='questioniom',
            name='hint',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='questionmoe',
            name='hint',
            field=models.TextField(default=None),
        ),
    ]
