# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_auto_20160115_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionioe',
            name='qfile',
            field=models.ImageField(default=None, upload_to=b'question/%y/%M/%d/%h/%s', blank=True),
        ),
    ]
