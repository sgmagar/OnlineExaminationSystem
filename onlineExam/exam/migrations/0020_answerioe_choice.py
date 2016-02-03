# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0019_auto_20160119_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerioe',
            name='choice',
            field=models.CharField(default=b'a', max_length=1, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd')]),
        ),
    ]
