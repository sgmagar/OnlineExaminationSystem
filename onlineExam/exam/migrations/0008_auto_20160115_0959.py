# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_questionioe_userquestionset'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestionset',
            name='qgroup',
            field=models.CharField(default=b'IOE', max_length=b'4', choices=[(b'IOE', b'IOE'), (b'IOM', b'IOM'), (b'MOE', b'MOE')]),
        ),
        migrations.AlterField(
            model_name='questionioe',
            name='qtype',
            field=models.CharField(default=b'Short', max_length=6, choices=[(b'Short', b'Short'), (b'Long', b'Long')]),
        ),
        migrations.AlterField(
            model_name='questionioe',
            name='subject',
            field=models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'Drawing', b'Drawing')]),
        ),
    ]
