# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('faculty', models.CharField(max_length=1, choices=[(b'D', b'Doctor'), (b'E', b'Engineer')])),
                ('news', models.TextField()),
                ('publishDate', models.DateField(auto_now=True)),
            ],
        ),
    ]
