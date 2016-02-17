# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0032_passchgkey_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionioe',
            name='subject',
            field=models.CharField(default=b'Physics', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'E-Aptitude', b'Engineering Aptitude Test')]),
        ),
        migrations.AlterField(
            model_name='questioniom',
            name='subject',
            field=models.CharField(default=b'Physics', max_length=12, choices=[(b'Physics', b'Physics'), (b'Chemistry', b'Chemistry'), (b'Zoology', b'Zoology'), (b'Botany', b'Botany')]),
        ),
        migrations.AlterField(
            model_name='questionmoe',
            name='subject',
            field=models.CharField(default=b'Physics', max_length=12, choices=[(b'Physics', b'Physics'), (b'Chemistry', b'Chemistry'), (b'Zoology', b'Zoology'), (b'Botany', b'Botany')]),
        ),
    ]
