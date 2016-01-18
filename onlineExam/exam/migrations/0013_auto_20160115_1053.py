# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_auto_20160115_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerioe',
            name='answer',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='questionioe',
            name='qfile',
            field=models.ImageField(default=None, upload_to=b'IOE/question/%Y/%M/%d/%h/%m/%s', blank=True),
        ),
        migrations.AlterField(
            model_name='questionioe',
            name='question',
            field=models.TextField(default=None, max_length=200),
        ),
    ]
