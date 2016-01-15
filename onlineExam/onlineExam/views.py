from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required


from exam.models import *
from .forms import *

def home(request):
	
	context = {
		"title":"Home"
	}
	return render(request,'home.html',context)
def classes(request):
	context={
		"title":"Classes"
	}
	return render(request,'classes.html',context)

def faq(request):
	context={
		"title":"FAQ"
	}
	return render(request,'faq.html',context)

def contactus(request):
	return redirect(reverse('home'))

def doctor(request):
	news = News.objects.filter(faculty__exact='D')[:5]
	context = {
		'title':'Doctor',
		'news':news
	}
	return render(request,'news.html',context)

def engineer(request):
	news = News.objects.filter(faculty__exact='E')[:5]
	context = {
		'title':'Engineer',
		'news':news
	}
	return render(request,'news.html',context)

def register(request):
	if request.method == 'POST':
		userform = UserForm(request.POST)
		profileform = UserProfileForm(request.POST)
		if userform.is_valid() and profileform.is_valid():
			user = userform.save(commit=False)
			user.set_password(userform.cleaned_data['password'])
			user.save()
			userprofile = profileform.save(commit=False)
			userprofile.user = user
			userprofile.save()
			context={
				"register":'Register Success'
			}
			return render(request,'register.html',context)
		context={
			"userForm":userform,
			"userProfileForm":profileform,
			"register": 'Register Here'
		}
	else:
		userForm = UserForm()
		userProfileForm = UserProfileForm()
		context={
			"userForm":userForm,
			"userProfileForm": userProfileForm,
			"register": 'Register Here'
		}
	return render(request,'register.html',context)

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				context={
					'login':'Login Success',
				}
				return render(request,'login.html',context)
		else:
			context={
				'login':'Login Here',
				'error':'Username or Password Invalid',
			}

	else:
		context={
			'login':'Login Here',
		}
	return render(request,'login.html',context)

@login_required(login_url='login')
def logout_view(request):
	logout(request)
	return redirect(reverse('home'))