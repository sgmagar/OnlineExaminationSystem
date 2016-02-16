# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0029_auto_20160210_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassChgKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=30)),
                ('expiry', models.DateTimeField(default=datetime.datetime(2016, 2, 16, 7, 27, 51, 670019))),
            ],
        ),
    ]
