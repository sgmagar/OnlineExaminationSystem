# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0035_auto_20160311_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passchgkey',
            name='key',
            field=models.CharField(max_length=150),
        ),
    ]
