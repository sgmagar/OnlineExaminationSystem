# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0018_auto_20160119_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionioe',
            name='questionset',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='questioniom',
            name='questionset',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='questionmoe',
            name='questionset',
            field=models.IntegerField(),
        ),
    ]
