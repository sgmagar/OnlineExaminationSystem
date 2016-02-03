# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from exam.models import *
# from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.forms import ModelForm

class UserForm(ModelForm):
	confirmpassword= forms.CharField(widget=forms.PasswordInput(attrs={'name':'confirmpassword','id':'confirmpassword','class':'form-control input-area','placeholder':'Confirm Password','autofocus':'autofocus', 'required':'required'})) 

	class Meta:
		model=User
		fields=['username','email','first_name','last_name','password']
		widgets={
			'username': forms.TextInput(attrs={'name':'username','id':'username','class':'form-control input-area','placeholder':'Username','autofocus':'autofocus','required':'required'}),
			'email': forms.EmailInput(attrs={'name':'email','id':'email','class':'form-control input-area','placeholder':'Email','autofocus':'autofocus','required':'required'}),
			'first_name': forms.TextInput(attrs={'name':'firstname','id':'firstname','class':'form-control input-area','placeholder':'First Name','autofocus':'autofocus','required':'required'}),
			'last_name': forms.TextInput(attrs={'name':'lastname','id':'lastname','class':'form-control input-area','placeholder':'Last Name','autofocus':'autofocus','required':'required'}),
			'password': forms.PasswordInput(attrs={'name':'password','id':'password','class':'form-control input-area','placeholder':'Password','autofocus':'autofocus','required':'required'})
		}
	def clean(self):
		cleaned_data = super(UserForm, self).clean()
		username = cleaned_data.get("username")
		email = cleaned_data.get("email")
		firstname = cleaned_data.get("first_name")
		lastname = cleaned_data.get("last_name")
		password = cleaned_data.get("password")
		confirmpassword =cleaned_data.get("confirmpassword")
		if password != confirmpassword:
			msg = 'Both password should watch'
			self.add_error('confirmpassword',msg)
		if email == "":
			msg = "This field is required"
			self.add_error('email',msg)
		return cleaned_data
		# if username == "":
		# 	raise forms.ValidationError("Username can't be empty")

class UserProfileForm(ModelForm):
	class Meta:
		model=UserProfile
		fields=['college','faculty','phone']
		# exclude=['user']
		widgets={
			'college':forms.TextInput(attrs={'name':'college','id':'college','class':'form-control input-area','placeholder':'College','autofocus':'autofocus','required':'required'}),
			'faculty':forms.Select(attrs={'class':'form-control'}),
			'phone':forms.TextInput(attrs={'name':'phone','id':'phone','class':'form-control input-area','placeholder':'Contact No.','autofocus':'autofocus','required':'required'}),

			# 'holiday_date':DateTimePicker(options={"format": "YYYY-MM-DD"}),
		}

	def clean(self):
		cleaned_data = super(UserProfileForm,self).clean()
		website = cleaned_data.get("college")
		phone = cleaned_data.get("phone")
		
			
		

