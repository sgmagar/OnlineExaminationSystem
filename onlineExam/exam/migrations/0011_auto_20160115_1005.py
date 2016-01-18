# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20160115_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquestionset',
            name='score',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
