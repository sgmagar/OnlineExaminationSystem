# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import exam.models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0030_passchgkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passchgkey',
            name='expiry',
            field=models.DateTimeField(default=exam.models.get_expiry),
        ),
    ]
