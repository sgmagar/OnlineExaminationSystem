# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *;

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	search_fields=['newstitle']
	ordering=('-publishDate',)

class UserProfileInline(admin.StackedInline):
    # list_display = ('user' 'website')
    # search_fields = ['user']
    # form = MyUserChangeForm
    # add_form = MyUserCreationForm
    model=UserProfile
    list_display=['college','faculty','phone','joined_date']
    can_delete = False
    verbose_name_plural = 'UserProfile'
class UserAdmin(BaseUserAdmin):
	BaseUserAdmin.list_display += ('get_college','get_faculty','get_date')
	inlines = (UserProfileInline,)
	list_filter = ('username',)
	search_fields = ('username',)
	ordering = ('-is_superuser','-is_active','username')

	def  get_college(self, obj):
		return UserProfile.objects.get(user=obj).college
	def get_faculty(self, obj):
		return UserProfile.objects.get(user=obj).faculty
	def get_phone(self, obj):
		return UserProfile.objects.get(user=obj).phone
	def get_date(self,obj):
		return UserProfile.objects.get(user=obj).joined_date

class KeyAdmin(admin.ModelAdmin):
	search_fields=['key']
	list_display=['key','status']

	ordering=('-status',)

class ChangePassKeyAdmin(admin.ModelAdmin):
	search_fields=['key']
	list_display=['key','email','expiry']

	ordering=('-expiry',)

class UserQuestionSetAdmin(admin.ModelAdmin):
	search_fields=['user']
	list_display=['user','questionset','status','score']
	ordering = ('user','questionset',)
	# def get_usernamee(self,obj):
	# 	return obj.user.username
# class AnswerIOEAdmin(admin.ModelAdmin):
# 	list_display = ['question','answer','value','afile']
# 	search_fields =['question']
# 	ordering=('question',)
class AnswerIOEInline(admin.TabularInline):
	model=AnswerIOE
	extra=0
	can_delete = False
	verbose_name_plural='AnswerIOE'
class QuestionIOEAdmin(admin.ModelAdmin):
	search_fields=['questionset','questionno','question']
	inlines = (AnswerIOEInline,)
	list_display=['questionset','questionno','subject','qtype','question','answer','qfile']
	ordering=('questionset','questionno',)

class AnswerIOMInline(admin.TabularInline):
	model=AnswerIOM
	extra=0
	can_delete = False
	verbose_name_plural='AnswerIOM'
class QuestionIOMAdmin(admin.ModelAdmin):
	search_fields=['questionset','questionno','question']
	inlines = (AnswerIOMInline,)
	list_display=['questionset','questionno','subject','qtype','question','answer','qfile']
	ordering=('questionset','questionno',)

class AnswerMOEInline(admin.TabularInline):
	model=AnswerMOE
	extra=0
	can_delete = False
	verbose_name_plural='AnswerMOE'
class QuestionMOEAdmin(admin.ModelAdmin):
	search_fields=['questionset','questionno','question']
	inlines = (AnswerMOEInline,)
	list_display=['questionset','questionno','subject','qtype','question','answer','qfile']
	ordering=('questionset','questionno',)
	

class FaqAdmin(admin.ModelAdmin):
	search_fields=['question']

class ContactUsAdmin(admin.ModelAdmin):
	search_fields=['message']


admin.site.register(News,NewsAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Key, KeyAdmin)
admin.site.register(UserQuestionSet,UserQuestionSetAdmin)
# admin.site.register(AnswerIOE,AnswerIOEAdmin)
admin.site.register(QuestionIOE,QuestionIOEAdmin)
admin.site.register(QuestionIOM,QuestionIOMAdmin)
admin.site.register(QuestionMOE,QuestionMOEAdmin)

admin.site.register(Faq, FaqAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ChangePassKey,ChangePassKeyAdmin)
admin.site.register(Domain)

