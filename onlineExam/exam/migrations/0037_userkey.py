# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import exam.models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0036_auto_20160311_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=150)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('expiry', models.DateTimeField(default=exam.models.get_expiry)),
            ],
        ),
    ]
