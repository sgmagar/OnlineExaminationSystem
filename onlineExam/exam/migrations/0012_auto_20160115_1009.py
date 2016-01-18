# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20160115_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerIOE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField()),
                ('value', models.BooleanField(default=False)),
                ('afile', models.ImageField(default=None, upload_to=b'IOE/answer/%y/%M/%d/%h/%m', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='questionioe',
            name='qfile',
            field=models.ImageField(default=None, upload_to=b'IOE/question/%y/%M/%d/%h/%s', blank=True),
        ),
        migrations.AddField(
            model_name='answerioe',
            name='question',
            field=models.ForeignKey(to='exam.QuestionIOE'),
        ),
    ]
