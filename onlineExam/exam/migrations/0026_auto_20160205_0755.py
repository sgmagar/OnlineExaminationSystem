# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0025_auto_20160201_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='newstitle',
            field=models.CharField(default=b'None', max_length=200),
        ),
        migrations.AlterField(
            model_name='news',
            name='faculty',
            field=models.CharField(default=b'IOE', max_length=4, choices=[(b'IOE', b'IOE'), (b'MOE', b'MOE'), (b'IOM', b'IOM')]),
        ),
    ]
