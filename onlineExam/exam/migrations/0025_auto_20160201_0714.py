# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0024_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='userquestionset',
            name='qgroup',
            field=models.CharField(default=b'IOE', max_length=4, choices=[(b'IOE', b'IOE'), (b'IOM', b'IOM'), (b'MOE', b'MOE')]),
        ),
    ]
