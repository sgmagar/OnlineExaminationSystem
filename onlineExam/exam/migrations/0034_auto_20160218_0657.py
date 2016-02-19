# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0033_auto_20160217_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questioniom',
            name='hint',
            field=models.TextField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='questionmoe',
            name='hint',
            field=models.TextField(default=None, blank=True),
        ),
    ]
