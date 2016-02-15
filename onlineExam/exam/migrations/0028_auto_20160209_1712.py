# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0027_auto_20160205_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerioe',
            name='hint',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='answeriom',
            name='hint',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='answermoe',
            name='hint',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='questionioe',
            name='question',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='questionioe',
            name='subject',
            field=models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'E-Aptitude', b'Engineering Aptitude Test')]),
        ),
    ]
