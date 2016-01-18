# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0016_auto_20160115_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='group',
            field=models.CharField(default=b'IOE', max_length=3, choices=[(b'IOE', b'IOE'), (b'IOM', b'IOM'), (b'MOE', b'MOE')]),
        ),
    ]
