# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import exam.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerIOE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd')])),
                ('answer', models.CharField(default=None, max_length=200)),
                ('afile', models.ImageField(default=None, upload_to=b'IOE/answer/%y/%m/%d/%H/%M/%S', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerIOM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd')])),
                ('answer', models.CharField(default=None, max_length=200)),
                ('afile', models.ImageField(default=None, upload_to=b'IOE/answer/%y/%m/%d/%H/%M/%S', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerMOE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd')])),
                ('answer', models.CharField(default=None, max_length=200)),
                ('afile', models.ImageField(default=None, upload_to=b'IOE/answer/%y/%m/%d/%H/%M/%S', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChangePassKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=150)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('expiry', models.DateTimeField(default=exam.models.get_expiry)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(default=None)),
                ('answer', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=40)),
                ('group', models.CharField(default=b'IOE', max_length=3, choices=[(b'IOE', b'IOE'), (b'IOM', b'IOM'), (b'MOE', b'MOE')])),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('faculty', models.CharField(default=b'IOE', max_length=4, choices=[(b'IOE', b'IOE'), (b'MOE', b'MOE'), (b'IOM', b'IOM')])),
                ('newstitle', models.CharField(default=b'None', max_length=200)),
                ('url', models.URLField(default=None)),
                ('publishDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionIOE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionset', models.IntegerField()),
                ('questionno', models.IntegerField()),
                ('subject', models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'E-Aptitude', b'Engineering Aptitude Test')])),
                ('qtype', models.CharField(default=b'Short', max_length=6, choices=[(b'Short', b'Short'), (b'Long', b'Long')])),
                ('question', models.TextField(default=None)),
                ('answer', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd')])),
                ('qfile', models.ImageField(default=None, upload_to=b'IOE/question/%y/%m/%d/%H/%M/%S', blank=True)),
                ('hint', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionIOM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionset', models.IntegerField()),
                ('questionno', models.IntegerField()),
                ('subject', models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'Drawing', b'Drawing')])),
                ('qtype', models.CharField(default=b'Short', max_length=6, choices=[(b'Short', b'Short'), (b'Long', b'Long')])),
                ('question', models.TextField(default=None, max_length=200)),
                ('answer', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd')])),
                ('qfile', models.ImageField(default=None, upload_to=b'IOE/question/%y/%m/%d/%H/%M/%S', blank=True)),
                ('hint', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionMOE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionset', models.IntegerField()),
                ('questionno', models.IntegerField()),
                ('subject', models.CharField(default=b'English', max_length=12, choices=[(b'Physics', b'Physics'), (b'Math', b'Math'), (b'English', b'English'), (b'Chemistry', b'Chemistry'), (b'Drawing', b'Drawing')])),
                ('qtype', models.CharField(default=b'Short', max_length=6, choices=[(b'Short', b'Short'), (b'Long', b'Long')])),
                ('question', models.TextField(default=None, max_length=200)),
                ('answer', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd')])),
                ('qfile', models.ImageField(default=None, upload_to=b'IOE/question/%y/%m/%d/%H/%M/%S', blank=True)),
                ('hint', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='UserKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=150)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('expiry', models.DateTimeField(default=exam.models.get_expiry)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('college', models.CharField(max_length=40, blank=True)),
                ('faculty', models.CharField(default=b'E', max_length=1, choices=[(b'E', b'Engineer'), (b'D', b'Doctor')])),
                ('phone', models.CharField(default=None, max_length=20)),
                ('joined_date', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestionSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qgroup', models.CharField(default=b'IOE', max_length=4, choices=[(b'IOE', b'IOE'), (b'IOM', b'IOM'), (b'MOE', b'MOE')])),
                ('questionset', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
        migrations.AddField(
            model_name='answerioe',
            name='question',
            field=models.ForeignKey(to='exam.QuestionIOE'),
        ),
    ]
