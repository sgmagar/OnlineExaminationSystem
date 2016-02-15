from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
	FACULTY_CHOICES = (
			('IOE','IOE'),
			('MOE','MOE'),
			('IOM','IOM'),
		)
	faculty = models.CharField(max_length=4, default='IOE', choices=FACULTY_CHOICES)
	newstitle = models.CharField(max_length=200, default='None')
	url= models.URLField( default=None)
	publishDate = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.newstitle

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
	GROUP_CHOICES=(
		('IOE','IOE'),
		('IOM','IOM'),
		('MOE','MOE'),
	)
	group = models.CharField(default='IOE', max_length=3, choices=GROUP_CHOICES)
	status = models.BooleanField(default=False)
	def __unicode__(self):
		return self.key

class Faq(models.Model):
	question = models.TextField(default=None)
	answer = models.TextField(default=None)

	def __unicode__(self):
		return self.question

class ContactUs(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField()
	message = models.TextField()


class UserQuestionSet(models.Model):
	user = models.ForeignKey(User)
	GROUP_CHOICES=(
		('IOE','IOE'),
		('IOM','IOM'),
		('MOE','MOE'),
	)
	qgroup = models.CharField(default='IOE',max_length=4, choices=GROUP_CHOICES)
	questionset=models.IntegerField()
	status = models.BooleanField(default=False)
	score = models.IntegerField(default=0,blank=True)

	def __unicode__(self):
		return unicode(self.questionset)

class QuestionIOE(models.Model):
	questionset = models.IntegerField()
	questionno = models.IntegerField()
	SUBJECT_CHOICES=(
			('Physics','Physics'),
			('Math','Math'),
			('English','English'),
			('Chemistry','Chemistry'),
			('E-Aptitude','Engineering Aptitude Test'),
		)
	subject = models.CharField(default='English',max_length=12, choices=SUBJECT_CHOICES)
	TYPE_CHOICES=(
			('Short','Short'),
			('Long','Long'),
		)
	qtype = models.CharField(default='Short',max_length=6, choices=TYPE_CHOICES)
	question = models.TextField(default=None)
	ANSWER_CHOICES=(
			('a','a'),
			('b','b'),
			('c','c'),
			('d','d'),
		)
	answer = models.CharField(max_length=1, default='a', choices=ANSWER_CHOICES)
	qfile = models.ImageField(default=None,blank=True, upload_to="IOE/question/%y/%m/%d/%H/%M/%S")
	hint = models.TextField(default=None)
	

	def __unicode__(self):
		return str(self.questionset)+" "+str(self.questionno)+" "+ self.subject+"\t"+self.question

class AnswerIOE(models.Model):
	question = models.ForeignKey(QuestionIOE)
	ANSWER_CHOICES=(
			('a','a'),
			('b','b'),
			('c','c'),
			('d','d'),
		)
	choice = models.CharField(max_length=1, default='a', choices=ANSWER_CHOICES)
	answer = models.CharField(max_length=200, default=None)
	
	afile = models.ImageField(default=None,blank=True, upload_to="IOE/answer/%y/%m/%d/%H/%M/%S")

class QuestionIOM(models.Model):
	questionset = models.IntegerField()
	questionno = models.IntegerField()
	SUBJECT_CHOICES=(
			('Physics','Physics'),
			('Math','Math'),
			('English','English'),
			('Chemistry','Chemistry'),
			('Drawing','Drawing'),
		)
	subject = models.CharField(default='English',max_length=12, choices=SUBJECT_CHOICES)
	TYPE_CHOICES=(
			('Short','Short'),
			('Long','Long'),
		)
	qtype = models.CharField(default='Short',max_length=6, choices=TYPE_CHOICES)
	question = models.TextField(default=None, max_length=200)
	ANSWER_CHOICES=(
			('a','a'),
			('b','b'),
			('c','c'),
			('d','d'),
		)
	answer = models.CharField(max_length=1, default='a', choices=ANSWER_CHOICES)
	qfile = models.ImageField(default=None,blank=True, upload_to="IOE/question/%y/%m/%d/%H/%M/%S")
	hint = models.TextField(default=None)
	def __unicode__(self):
		return str(self.questionset)+" "+str(self.questionno)+" "+ self.subject+"\t"+self.question

class AnswerIOM(models.Model):
	question = models.ForeignKey(QuestionIOM)
	ANSWER_CHOICES=(
			('a','a'),
			('b','b'),
			('c','c'),
			('d','d'),
		)
	choice = models.CharField(max_length=1, default='a', choices=ANSWER_CHOICES)
	answer = models.CharField(max_length=200, default=None)
	afile = models.ImageField(default=None,blank=True, upload_to="IOE/answer/%y/%m/%d/%H/%M/%S")

class QuestionMOE(models.Model):
	questionset = models.IntegerField()
	questionno = models.IntegerField()
	SUBJECT_CHOICES=(
			('Physics','Physics'),
			('Math','Math'),
			('English','English'),
			('Chemistry','Chemistry'),
			('Drawing','Drawing'),
		)
	subject = models.CharField(default='English',max_length=12, choices=SUBJECT_CHOICES)
	TYPE_CHOICES=(
			('Short','Short'),
			('Long','Long'),
		)
	qtype = models.CharField(default='Short',max_length=6, choices=TYPE_CHOICES)
	question = models.TextField(default=None, max_length=200)
	ANSWER_CHOICES=(
			('a','a'),
			('b','b'),
			('c','c'),
			('d','d'),
		)
	answer = models.CharField(max_length=1, default='a', choices=ANSWER_CHOICES)
	qfile = models.ImageField(default=None,blank=True, upload_to="IOE/question/%y/%m/%d/%H/%M/%S")
	hint = models.TextField(default=None)
	def __unicode__(self):
		return str(self.questionset)+" "+str(self.questionno)+" "+ self.subject+"\t"+self.question

class AnswerMOE(models.Model):
	question = models.ForeignKey(QuestionMOE)
	ANSWER_CHOICES=(
			('a','a'),
			('b','b'),
			('c','c'),
			('d','d'),
		)
	choice = models.CharField(max_length=1, default='a', choices=ANSWER_CHOICES)
	answer = models.CharField(max_length=200, default=None)
	
	afile = models.ImageField(default=None,blank=True, upload_to="IOE/answer/%y/%m/%d/%H/%M/%S")




# Question:
# questionset,qusetionno,subect,type,quesiton_text,type,file

# answer:
# 	question, answer,check,file
	
