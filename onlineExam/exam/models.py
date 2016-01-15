from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
	FACULTY_CHOICES = (
			('Doctor','Doctor'),
			('Engineer','Engineer'),
		)
	faculty = models.CharField(max_length=10,choices=FACULTY_CHOICES)
	news = models.TextField()
	publishDate = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.news

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	college = models.CharField(blank=True, max_length=40)
	FACULTY_CHOICES = (
			('E','Engineer'),
			('D','Doctor'),
		)
	faculty = models.CharField(default='E',max_length=1, choices=FACULTY_CHOICES)
	phone = models.CharField(default=None,max_length=20)
	joined_date = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.user.username

class Key(models.Model):
	key = models.CharField(blank=False, max_length=40)
	status = models.BooleanField(default=False)
	def __unicode__(self):
		return self.key
class UserQuestionSet(models.Model):
	user = models.ForeignKey(User)
	questionset=models.IntegerField()
	status = models.BooleanField(default=False)
	score = models.IntegerField(default=None)

class QuestionSet(models.Model):
	questionset = models.IntegerField()
	SUBJECT_CHOICES=(
			('Physics','Physics'),
			('Math','Math'),
			('English','English')
		)



# Question:
# set,subect,quesiton_text,type,file

# answer:
# 	question, answer,check,file
	
