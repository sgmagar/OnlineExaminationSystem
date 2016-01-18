# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0014_auto_20160115_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerioe',
            name='afile',
            field=models.ImageField(default=None, upload_to=b'IOE/answer/%y/%m/%d/%H/%M/%S', blank=True),
        ),
    ]
