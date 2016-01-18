from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from importlib import import_module
from django.conf import settings
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
session = SessionStore()


from exam.models import *
from .forms import *

def home(request):
	request.session['rechargeError']=None
	request.session['qsetError']=None
	
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
				print user.id
				return redirect(reverse('dashboard' , args=(user.id,)))
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

@login_required(login_url='login')
def dashboard(request, id):
	user = get_object_or_404(User,pk=id)
	ioe_questionset = request.user.userquestionset_set.filter(qgroup='IOE').order_by('questionset')
	iom_questionset = request.user.userquestionset_set.filter(qgroup='IOM').order_by('questionset')
	moe_questionset = request.user.userquestionset_set.filter(qgroup='MOE').order_by('questionset')

	print len(ioe_questionset)
	context={
		'title':'Dashboard',
		'rechargeError': request.session['rechargeError'],
		'qsetError': request.session['qsetError'],
		'ioe_questionset':ioe_questionset,
		'iom_questionset':iom_questionset,
		'moe_questionset':moe_questionset,

	}
	request.session['rechargeError']=None
	request.session['qsetError']=None
	return render(request,'dashboard.html',context)

@login_required(login_url='login')
def recharge(request):
	if request.method=='POST':
		group = request.POST['group']
		pin = request.POST['pin']
		user = request.user;
		key = Key.objects.filter(group=group,key=pin,status=False)
		
		print key
		if  not key:
			request.session['rechargeError']='Key is invalid'
			# print request.session['rechargeError']
		else:
			qset = user.userquestionset_set.filter(qgroup=group).count()
			for i in range(1,11):
				userquestionset=UserQuestionSet.objects.create(user=user,qgroup=group,questionset=qset+i)
				userquestionset.save()
			key[0].status=True
			key[0].save()


	return redirect(reverse('dashboard', args=(request.user.id,)))
@login_required(login_url='login')
def questionset(request,qgroup,qset):
	if qgroup.strip() == 'IOE':
		if(len(request.user.userquestionset_set.filter(qgroup='IOE',questionset=qset))>0):
			print qgroup,qset
			return HttpResponse("Your group is "+qgroup+" and questionset is "+qset)
		else:
			request.session['qsetError']="You don't have acces to this question"
			return redirect(reverse('dashboard' ,args=(request.user.id,)))
	if qgroup.strip() == 'IOM':
		if(len(request.user.userquestionset_set.filter(qgroup='IOM',questionset=qset))>0):
			print qgroup,qset
			return HttpResponse("Your group is "+qgroup+" and questionset is "+qset)
		else:
			request.session['qsetError']="You don't have acces to this question"
			return redirect(reverse('dashboard' ,args=(request.user.id,)))
	if qgroup.strip() == 'MOE':
		if(len(request.user.userquestionset_set.filter(qgroup='MOE',questionset=qset))>0):
			print qgroup,qset
			return HttpResponse("Your group is "+qgroup+" and questionset is "+qset)
		else:
			request.session['qsetError']="You don't have acces to this question"
			return redirect(reverse('dashboard' ,args=(request.user.id,)))

