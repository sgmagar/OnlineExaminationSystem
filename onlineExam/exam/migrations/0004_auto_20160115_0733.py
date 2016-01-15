# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20160115_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='college',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
