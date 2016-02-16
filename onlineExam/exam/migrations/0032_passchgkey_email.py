# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0031_auto_20160216_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='passchgkey',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
