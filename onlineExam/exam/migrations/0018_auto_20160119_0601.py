# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0017_key_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionioe',
            name='questionno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='questioniom',
            name='questionno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='questionmoe',
            name='questionno',
            field=models.IntegerField(),
        ),
    ]
