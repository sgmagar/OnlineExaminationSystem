# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20160115_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='faculty',
            field=models.CharField(max_length=10, choices=[(b'Doctor', b'Doctor'), (b'Engineer', b'Engineer')]),
        ),
    ]
