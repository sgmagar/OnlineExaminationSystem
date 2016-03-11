# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0034_auto_20160218_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionioe',
            name='subject',
            field=models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'E-Aptitude', b'Engineering Aptitude Test')]),
        ),
        migrations.AlterField(
            model_name='questioniom',
            name='hint',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='questioniom',
            name='subject',
            field=models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'Drawing', b'Drawing')]),
        ),
        migrations.AlterField(
            model_name='questionmoe',
            name='hint',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='questionmoe',
            name='subject',
            field=models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'Drawing', b'Drawing')]),
        ),
    ]
