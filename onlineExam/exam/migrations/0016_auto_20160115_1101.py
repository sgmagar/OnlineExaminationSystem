# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0015_auto_20160115_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerIOM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(default=None, max_length=200)),
                ('value', models.BooleanField(default=False)),
                ('afile', models.ImageField(default=None, upload_to=b'IOE/answer/%y/%m/%d/%H/%M/%S', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerMOE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(default=None, max_length=200)),
                ('value', models.BooleanField(default=False)),
                ('afile', models.ImageField(default=None, upload_to=b'IOE/answer/%y/%m/%d/%H/%M/%S', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionIOM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionset', models.IntegerField(unique=True)),
                ('questionno', models.IntegerField(unique=True)),
                ('subject', models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'Drawing', b'Drawing')])),
                ('qtype', models.CharField(default=b'Short', max_length=6, choices=[(b'Short', b'Short'), (b'Long', b'Long')])),
                ('question', models.TextField(default=None, max_length=200)),
                ('qfile', models.ImageField(default=None, upload_to=b'IOE/question/%y/%m/%d/%H/%M/%S', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionMOE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionset', models.IntegerField(unique=True)),
                ('questionno', models.IntegerField(unique=True)),
                ('subject', models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'Drawing', b'Drawing')])),
                ('qtype', models.CharField(default=b'Short', max_length=6, choices=[(b'Short', b'Short'), (b'Long', b'Long')])),
                ('question', models.TextField(default=None, max_length=200)),
                ('qfile', models.ImageField(default=None, upload_to=b'IOE/question/%y/%m/%d/%H/%M/%S', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='answermoe',
            name='question',
            field=models.ForeignKey(to='exam.QuestionMOE'),
        ),
        migrations.AddField(
            model_name='answeriom',
            name='question',
            field=models.ForeignKey(to='exam.QuestionIOM'),
        ),
    ]
