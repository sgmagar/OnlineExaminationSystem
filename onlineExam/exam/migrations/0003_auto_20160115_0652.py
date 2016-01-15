# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='faculty',
            field=models.CharField(default=b'E', max_length=1, choices=[(b'E', b'Engineer'), (b'D', b'Doctor')]),
        ),
    ]
