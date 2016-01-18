# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0006_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionIOE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionset', models.IntegerField(unique=True)),
                ('questionno', models.IntegerField(unique=True)),
                ('subject', models.CharField(max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'Drawing', b'Drawing')])),
                ('qtype', models.CharField(max_length=6, choices=[(b'Short', b'Short'), (b'Long', b'Long')])),
                ('question', models.TextField(default=None)),
                ('qfile', models.ImageField(default=None, upload_to=b'question/%y/%M/%d/%h/%s')),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestionSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionset', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=None)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
