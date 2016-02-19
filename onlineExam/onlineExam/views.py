# -*- coding: utf-8 -*-
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

from django.core import serializers
from django.core.mail import send_mail
import random
import json

from exam.models import *
from .forms import *

from django.views.decorators.csrf import csrf_exempt  

def home(request):
	request.session['rechargeError']=None
	request.session['qsetError']=None
	request.session['key'] = None
	if request.user.is_authenticated():
		return redirect(reverse('dashboard', args=(request.user.id,)))

	context = {
		"title":"Home"
	}
	return render(request,'home.html',context)

def about(request):
	context = {
		'title': 'About Us',
	}
	return render(request, 'about.html', context)
def classes(request):
	context={
		"title":"Classes"
	}
	return render(request,'classes.html',context)

def faq(request):
	faq = Faq.objects.all()
	context={
		"title":"FAQ",
		'faq': faq,
	}
	return render(request,'faq.html',context)

def contactus(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']

		contactus = ContactUs.objects.create(name=name, email=email, message=message)
		contactus.save()
	context={
		'title':'Contact Us',
	}
	return render(request, 'contact.html',context)

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
	request.session['rechargeError']=None
	request.session['qsetError']=None
	request.session['key'] = None
	if request.method == 'POST':
		userform = UserForm(request.POST)
		profileform = UserProfileForm(request.POST)
		if userform.is_valid() and profileform.is_valid():
			user = userform.save(commit=False)
			user.set_password(userform.cleaned_data['password'])
			test_user = None
			try :
				test_user = User.objects.get(email=user.email)
			except Exception as e:
				pass
			if test_user != None:
				context={
					'title':'Register',
					"error":'Email already exists'
				}
				return render(request,'register.html',context)
			user.save()
			userprofile = profileform.save(commit=False)
			userprofile.user = user
			userprofile.save()
			context={
				'title':'Register',
				"register":'Register Success',
				
			}
			return render(request,'register.html',context)
		context={
			'title':'Register',
			"userForm":userform,
			"userProfileForm":profileform,
			"register": 'Register Here'
		}
	else:
		userForm = UserForm()
		userProfileForm = UserProfileForm()
		context={
			'title':'Register',
			"userForm":userForm,
			"userProfileForm": userProfileForm,
			"register": 'Register Here'
		}
	return render(request,'register.html',context)

def login_view(request):
	request.session['rechargeError']=None
	request.session['qsetError']=None
	request.session['key'] = None
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		if '@' in username:
			try:
				username = User.objects.get(email=username).username
			except Exception as e:
				pass
			
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request, user)
				context={
					'title':'Login',
					'login':'Login Success',
				}
				print user.id
				return redirect(reverse('dashboard' , args=(user.id,)))
		else:
			context={
				'title':'Login',
				'login':'Login Here',
				'error':'Username or Password Invalid',
			}

	else:
		context={
			'title':'Login',
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
	if request.user == user:
		ioe_questionset = request.user.userquestionset_set.filter(qgroup='IOE').order_by('questionset')
		iom_questionset = request.user.userquestionset_set.filter(qgroup='IOM').order_by('questionset')
		moe_questionset = request.user.userquestionset_set.filter(qgroup='MOE').order_by('questionset')
		ioe_questionset_1 = ioe_questionset[:10]
		ioe_questionset_2 = ioe_questionset[10:20]
		ioe_questionset_3 = ioe_questionset[20:30]
		ioe_questionset_4 = ioe_questionset[30:40]
		ioe_questionset_5 = ioe_questionset[40:50]
		iom_questionset_1 = iom_questionset[:10]
		iom_questionset_2 = iom_questionset[10:20]
		iom_questionset_3 = iom_questionset[20:30]
		iom_questionset_4 = iom_questionset[30:40]
		iom_questionset_5 = iom_questionset[40:50]
		moe_questionset_1 = moe_questionset[:10]
		moe_questionset_2 = moe_questionset[10:20]
		moe_questionset_3 = moe_questionset[20:30]
		moe_questionset_4 = moe_questionset[30:40]
		moe_questionset_5 = moe_questionset[40:50]
		# ioefreeset = QuestionIOE.objects.filter(questionset=150)
		# moefreeset = QuestionMOE.objects.filter(questionset=150)
		# iomfreeset = QuestionIOM.objects.filter(questionset=150)
		# print ioefreeset.questionset

		print len(ioe_questionset)
		context={
			'title':'Dashboard',
			'rechargeError': request.session['rechargeError'],
			'qsetError': request.session['qsetError'],
			'firstname':user.first_name,
			'ioe_questionset_1': ioe_questionset_1,
			'ioe_questionset_2': ioe_questionset_2,
			'ioe_questionset_3': ioe_questionset_3,
			'ioe_questionset_4': ioe_questionset_4,
			'ioe_questionset_5': ioe_questionset_5,
			'iom_questionset_1': iom_questionset_1,
			'iom_questionset_2': iom_questionset_2,
			'iom_questionset_3': iom_questionset_3,
			'iom_questionset_4': iom_questionset_4,
			'iom_questionset_5': iom_questionset_5,
			'moe_questionset_1': moe_questionset_1,
			'moe_questionset_2': moe_questionset_2,
			'moe_questionset_3': moe_questionset_3,
			'moe_questionset_4': moe_questionset_4,
			'moe_questionset_5': moe_questionset_5,
			# 'ioefreeset':ioefreeset,
			# 'moefreeset':moefreeset,
			# 'iomfreeset':iomfreeset,

		}
		request.session['rechargeError']=None
		request.session['qsetError']=None
		return render(request,'dashboard.html',context)
	else:
		return redirect(reverse('home'))

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
			if qset <=50:
				for i in range(1,11):
					userquestionset=UserQuestionSet.objects.create(user=user,qgroup=group,questionset=qset+i)
					userquestionset.save()
				key[0].status=True
				key[0].save()


	return redirect(reverse('dashboard', args=(request.user.id,)))
@login_required(login_url='login')
def questionset(request,qgroup,qset):
	if qgroup.strip() == 'IOE':
		if len(request.user.userquestionset_set.filter(qgroup='IOE',questionset=qset))>0 or qset==str(150):
			question = QuestionIOE.objects.filter(questionset=qset).order_by('questionno')
			first_group = question[:10]
			second_group = question[10:20] 
			third_group = question[20:30]
			fourth_group = question[30:40]
			fifth_group = question[40:50]
			sixth_group = question[50:60]
			seventh_group = question[60:70]
			eighth_group = question[70:80]
			nineth_group = question[80:90]
			tenth_group = question[90:100]
			context={
				'first_group':first_group,
				'second_group':second_group,
				'third_group':third_group,
				'fourth_group':fourth_group,
				'fifth_group': fifth_group,
				'sixth_group': sixth_group,
				'seventh_group': seventh_group,
				'eighth_group': eighth_group,
				'nineth_group': nineth_group,
				'tenth_group': tenth_group,
				'qgroup':qgroup,
				'qset':qset,
			}
			return render(request,'questionset_ioe.html',context)
		else:
			request.session['qsetError']="You don't have acces to this question"
			return redirect(reverse('dashboard' ,args=(request.user.id,)))
	if qgroup.strip() == 'IOM':
		if(len(request.user.userquestionset_set.filter(qgroup='IOM',questionset=qset,status=False))>0) or qset==str(150):
			question = QuestionIOM.objects.filter(questionset=qset).order_by('questionno')
			first_group = question[:10]
			second_group = question[10:20] 
			third_group = question[20:30]
			fourth_group = question[30:40]
			fifth_group = question[40:50]
			sixth_group = question[50:60]
			seventh_group = question[60:70]
			eighth_group = question[70:80]
			nineth_group = question[80:90]
			tenth_group = question[90:100]
			context={
				'first_group':first_group,
				'second_group':second_group,
				'third_group':third_group,
				'fourth_group':fourth_group,
				'fifth_group': fifth_group,
				'sixth_group': sixth_group,
				'seventh_group': seventh_group,
				'eighth_group': eighth_group,
				'nineth_group': nineth_group,
				'tenth_group': tenth_group,
				'qgroup':qgroup,
				'qset':qset,
			}
			return render(request,'questionset_iom.html',context)
		else:
			request.session['qsetError']="You don't have acces to this question"
			return redirect(reverse('dashboard' ,args=(request.user.id,)))
	if qgroup.strip() == 'MOE':
		if(len(request.user.userquestionset_set.filter(qgroup='MOE',questionset=qset,status=False))>0) or qset==str(150):
			question = QuestionMOE.objects.filter(questionset=qset).order_by('questionno')
			first_group = question[:10]
			second_group = question[10:20] 
			third_group = question[20:30]
			fourth_group = question[30:40]
			fifth_group = question[40:50]
			sixth_group = question[50:60]
			seventh_group = question[60:70]
			eighth_group = question[70:80]
			nineth_group = question[80:90]
			tenth_group = question[90:100]
			context={
				'first_group':first_group,
				'second_group':second_group,
				'third_group':third_group,
				'fourth_group':fourth_group,
				'fifth_group': fifth_group,
				'sixth_group': sixth_group,
				'seventh_group': seventh_group,
				'eighth_group': eighth_group,
				'nineth_group': nineth_group,
				'tenth_group': tenth_group,
				'qgroup':qgroup,
				'qset':qset,
			}
			return render(request,'questionset_moe.html',context)
		else:
			request.session['qsetError']="You don't have acces to this question"
			return redirect(reverse('dashboard' ,args=(request.user.id,)))


@login_required(login_url='login')
def checkset(request, qgroup, qset):
	
	if request.method == 'POST':
		print request.POST
		
		if qgroup == 'IOM':
			wrong=[]
			not_attempted = []
			correct = []
			total = 100
			physics_total = 20
			physics_attempted = 0
			physics_correct = 0
			physics_mark = 0
			chemistry_total = 30
			chemistry_attempted = 0
			chemistry_correct = 0
			chemistry_mark = 0
			zoology_total = 30
			zoology_attempted = 0
			zoology_correct = 0
			zoology_mark = 0
			botany_total = 20
			botany_attempted = 0
			botany_correct = 0
			botany_mark = 0
			questionIOM = QuestionIOM.objects.filter(questionset=qset).order_by('questionno')
			for i in range(1,101):
				if i<=20:
					try:
						if request.POST[str(i)]:
							physics_attempted +=1

							if request.POST[str(i)] == questionIOM[i-1].answer:
								correct.append(i)
								physics_correct += 1
								physics_mark +=1	
												
							else:
								wrong.append(i)

					except Exception as ex:
						not_attempted.append(i)

				elif i<=50:
					try:
						if request.POST[str(i)]:
							chemistry_attempted +=1
							
							if request.POST[str(i)] == questionIOM[i-1].answer:
								correct.append(i)
								chemistry_correct += 1
								chemistry_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)

				elif i<=80:
					try:
						if request.POST[str(i)]:
							zoology_attempted +=1
							
							if request.POST[str(i)] == questionIOM[i-1].answer:
								correct.append(i)
								zoology_correct += 1
								zoology_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				elif i<=100:
					try:
						if request.POST[str(i)]:
							botany_attempted +=1
							
							if request.POST[str(i)] == questionIOM[i-1].answer:
								correct.append(i)
								botany_correct += 1
								botany_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				else:
					pass

		
			request.session['checked_questions'] = {'qgroup':qgroup,'qset':qset,'wrong':wrong,
				'not_attempted':not_attempted,'correct':correct}
			if qset != str(150):
				userquestionset = request.user.userquestionset_set.get(qgroup=qgroup, questionset=qset)
				userquestionset.score = physics_mark + chemistry_mark + zoology_mark + botany_mark
				userquestionset.status = True 
				userquestionset.save()
			score = {
				'qgroup':qgroup,
				'qset': qset,
				'physics_total': physics_total,
				'physics_attempted': physics_attempted,
				'physics_correct': physics_correct,
				'physics_mark': physics_mark,
				'chemistry_total': chemistry_total,
				'chemistry_attempted': chemistry_attempted,
				'chemistry_correct': chemistry_correct,
				'chemistry_mark': chemistry_mark,
				'zoology_total': zoology_total,
				'zoology_attempted': zoology_attempted,
				'zoology_correct': zoology_correct,
				'zoology_mark': zoology_mark,
				'botany_total': botany_total,
				'botany_attempted': botany_attempted,
				'botany_correct': botany_correct,
				'botany_mark': botany_mark,
				'total': total,
				'total_attempted': physics_attempted + chemistry_attempted + zoology_attempted + botany_attempted,
				'total_correct': physics_correct + chemistry_correct + zoology_correct + botany_correct,
				'total_mark': physics_mark + chemistry_mark + zoology_mark + botany_mark,
			}
			request.session["solution"] = "okay"
			return render(request, 'result_iom.html', score)

		elif qgroup == 'IOE':
			wrong=[]
			not_attempted = []
			correct = []
			total = 100
			physics_total = 25
			physics_attempted = 0
			physics_correct = 0
			physics_mark = 0
			math_total = 25
			math_attempted = 0
			math_correct = 0
			math_mark = 0
			chemistry_total = 16
			chemistry_attempted = 0
			chemistry_correct = 0
			chemistry_mark = 0
			english_total = 18
			english_attempted = 0
			english_correct = 0
			english_mark = 0
			eaptitude_total = 16
			eaptitude_attempted = 0
			eaptitude_correct = 0
			eaptitude_mark = 0
			questionIOE = QuestionIOE.objects.filter(questionset=qset).order_by('questionno')
			for i in range(1,101):
				if i<=10:
					try:
						if request.POST[str(i)]:
							physics_attempted +=1

							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								physics_correct += 1
								physics_mark +=1	
												
							else:
								wrong.append(i)

					except Exception as ex:
						not_attempted.append(i)

				elif i<=20:
					try:
						if request.POST[str(i)]:
							math_attempted +=1
							
							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								math_correct += 1
								math_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)

				elif i<=32:
					try:
						if request.POST[str(i)]:
							chemistry_attempted +=1
							
							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								chemistry_correct += 1
								chemistry_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				elif i<=46:
					try:
						if request.POST[str(i)]:
							english_attempted +=1
							
							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								english_correct += 1
								english_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				elif i<=60:
					try:
						if request.POST[str(i)]:
							eaptitude_attempted +=1
							
							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								eaptitude_correct += 1
								eaptitude_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				elif i<=75:
					try:
						if request.POST[str(i)]:
							physics_attempted +=1
							
							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								physics_correct += 1
								physics_mark +=2	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				elif i<=90:
					try:
						if request.POST[str(i)]:
							math_attempted +=1
							
							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								math_correct += 1
								math_mark +=2	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				elif i<=94:
					try:
						if request.POST[str(i)]:
							chemistry_attempted +=1
							
							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								chemistry_correct += 1
								chemistry_mark +=2	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				elif i<=98:
					try:
						if request.POST[str(i)]:
							english_attempted +=1
							
							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								english_correct += 1
								english_mark +=2	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				elif i<=100:
					try:
						if request.POST[str(i)]:
							eaptitude_attempted +=1
							
							if request.POST[str(i)] == questionIOE[i-1].answer:
								correct.append(i)
								eaptitude_correct += 1
								eaptitude_mark +=2	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				else:
					pass

		
			request.session['checked_questions'] = {'qgroup':qgroup,'qset':qset,'wrong':wrong,
				'not_attempted':not_attempted,'correct':correct}
			if qset != str(150):
				userquestionset = request.user.userquestionset_set.get(qgroup=qgroup, questionset=qset)
				userquestionset.score = physics_mark + math_mark + chemistry_mark + english_mark+eaptitude_mark
				userquestionset.status = True 
				userquestionset.save()
			score = {
				'qgroup':qgroup,
				'qset': qset,
				'physics_total': physics_total,
				'physics_attempted': physics_attempted,
				'physics_correct': physics_correct,
				'physics_mark': physics_mark,
				'math_total': math_total,
				'math_attempted': math_attempted,
				'math_correct': math_correct,
				'math_mark': math_mark,
				'chemistry_total': chemistry_total,
				'chemistry_attempted': chemistry_attempted,
				'chemistry_correct': chemistry_correct,
				'chemistry_mark': chemistry_mark,
				'english_total': english_total,
				'english_attempted': english_attempted,
				'english_correct': english_correct,
				'english_mark': english_mark,
				'eaptitude_total': eaptitude_total,
				'eaptitude_attempted':eaptitude_attempted,
				'eaptitude_correct':eaptitude_correct,
				'eaptitude_mark':eaptitude_mark,
				'total': total,
				'total_attempted': physics_attempted + math_attempted + chemistry_attempted + english_attempted+eaptitude_attempted,
				'total_correct': physics_correct + math_correct + chemistry_correct + english_correct+eaptitude_correct,
				'total_mark': physics_mark + math_mark + chemistry_mark + english_mark+eaptitude_mark,
			}
			request.session["solution"] = "okay"
			return render(request, 'result_ioe.html', score)
		if qgroup == 'MOE':
			wrong=[]
			not_attempted = []
			correct = []
			total = 100
			physics_total = 30
			physics_attempted = 0
			physics_correct = 0
			physics_mark = 0
			chemistry_total = 30
			chemistry_attempted = 0
			chemistry_correct = 0
			chemistry_mark = 0
			zoology_total = 20
			zoology_attempted = 0
			zoology_correct = 0
			zoology_mark = 0
			botany_total = 20
			botany_attempted = 0
			botany_correct = 0
			botany_mark = 0
			questionMOE = QuestionMOE.objects.filter(questionset=qset).order_by('questionno')
			for i in range(1,101):
				if i<=30:
					try:
						if request.POST[str(i)]:
							physics_attempted +=1

							if request.POST[str(i)] == questionMOE[i-1].answer:
								correct.append(i)
								physics_correct += 1
								physics_mark +=1	
												
							else:
								wrong.append(i)

					except Exception as ex:
						not_attempted.append(i)

				elif i<=60:
					try:
						if request.POST[str(i)]:
							chemistry_attempted +=1
							
							if request.POST[str(i)] == questionMOE[i-1].answer:
								correct.append(i)
								chemistry_correct += 1
								chemistry_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)

				elif i<=80:
					try:
						if request.POST[str(i)]:
							zoology_attempted +=1
							
							if request.POST[str(i)] == questionMOE[i-1].answer:
								correct.append(i)
								zoology_correct += 1
								zoology_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				elif i<=100:
					try:
						if request.POST[str(i)]:
							botany_attempted +=1
							
							if request.POST[str(i)] == questionMOE[i-1].answer:
								correct.append(i)
								botany_correct += 1
								botany_mark +=1	
													
							else:
								wrong.append(i)
					except Exception as ex:
						not_attempted.append(i)
				else:
					pass

		
			request.session['checked_questions'] = {'qgroup':qgroup,'qset':qset,'wrong':wrong,
				'not_attempted':not_attempted,'correct':correct}
			if qset != str(150):
				userquestionset = request.user.userquestionset_set.get(qgroup=qgroup, questionset=qset)
				userquestionset.score = physics_mark + chemistry_mark + zoology_mark + botany_mark
				userquestionset.status = True 
				userquestionset.save()
			score = {
				'qgroup':qgroup,
				'qset': qset,
				'physics_total': physics_total,
				'physics_attempted': physics_attempted,
				'physics_correct': physics_correct,
				'physics_mark': physics_mark,
				'chemistry_total': chemistry_total,
				'chemistry_attempted': chemistry_attempted,
				'chemistry_correct': chemistry_correct,
				'chemistry_mark': chemistry_mark,
				'zoology_total': zoology_total,
				'zoology_attempted': zoology_attempted,
				'zoology_correct': zoology_correct,
				'zoology_mark': zoology_mark,
				'botany_total': botany_total,
				'botany_attempted': botany_attempted,
				'botany_correct': botany_correct,
				'botany_mark': botany_mark,
				'total': total,
				'total_attempted': physics_attempted + chemistry_attempted + zoology_attempted + botany_attempted,
				'total_correct': physics_correct + chemistry_correct + zoology_correct + botany_correct,
				'total_mark': physics_mark + chemistry_mark + zoology_mark + botany_mark,
			}
			request.session["solution"] = "okay"
			return render(request, 'result_moe.html', score)
		else:
			pass
		
		# score = json.dumps(score)
		
					

	else:
		return redirect(reverse('dashboard', args=(request.user.id,) ))

def solution(request, qgroup, qset):
	if request.session['checked_questions']['qset'] == qset:
		if request.session['checked_questions']['qgroup'] == 'IOE':
			questionIOE = QuestionIOE.objects.filter(questionset=qset).order_by('questionno')
			for question in questionIOE:
				if question.questionno in request.session['checked_questions']['wrong']:
					question.status = 'wrong'
				elif question.questionno in request.session['checked_questions']['not_attempted']:
					question.status = 'not_attempted'
				elif question.questionno in request.session['checked_questions']['correct']:
					question.status = 'correct'
				else:
					pass
			context = {
				'qgroup': qgroup,
				'questionIOE': questionIOE,
				'title': 'Solution',
			}
			return render(request, 'solution.html', context)
		elif request.session['checked_questions']['qgroup'] == 'IOM':
			questionIOM = QuestionIOM.objects.filter(questionset=qset).order_by('questionno')
			for question in questionIOM:
				if question.questionno in request.session['checked_questions']['wrong']:
					question.status = 'wrong'
				elif question.questionno in request.session['checked_questions']['not_attempted']:
					question.status = 'not_attempted'
				elif question.questionno in request.session['checked_questions']['correct']:
					question.status = 'correct'
				else:
					pass
			context = {
				'qgroup': qgroup,
				'questionIOM': questionIOM,
				'title': 'Solution',
			}
			return render(request, 'solution.html', context)
		elif request.session['checked_questions']['qgroup'] == 'MOE':
			questionMOE = QuestionMOE.objects.filter(questionset=qset).order_by('questionno')
			for question in questionMOE:
				if question.questionno in request.session['checked_questions']['wrong']:
					question.status = 'wrong'
				elif question.questionno in request.session['checked_questions']['not_attempted']:
					question.status = 'not_attempted'
				elif question.questionno in request.session['checked_questions']['correct']:
					question.status = 'correct'
				else:
					pass
			context = {
				'qgroup': qgroup,
				'questionMOE': questionMOE,
				'title': 'Solution',
			}
			return render(request, 'solution.html', context)
		else:
			return redirect(reverse('dashboard' ,args=(request.user.id,)))	
	else:
		return redirect(reverse('dashboard' ,args=(request.user.id,)))

@login_required(login_url='login')
def rules(request, qgroup, qset):
	if qgroup=='IOE':
		if len(request.user.userquestionset_set.filter(qgroup='IOE',questionset=qset))>0 or qset==str(150):
			context={
				'title':'Rules',
				'firstname':request.user.first_name,
				'qgroup': qgroup,
				'qset':qset,

			}
			return render(request,'rules_ioe.html', context)
		else:
			context = {
				'error': "You don't have access to this question set",
				'title':'Rules',
				'firstname':request.user.first_name,
				'qgroup': qgroup,
				'qset':qset,
			}
			return render(request,'rules_ioe.html', context)
	if qgroup=='IOM':
		if len(request.user.userquestionset_set.filter(qgroup='IOM',questionset=qset))>0 or qset==str(150):
			context={
				'title':'Rules',
				'firstname':request.user.first_name,
				'qgroup': qgroup,
				'qset':qset,

			}
			return render(request,'rules_iom.html', context)
		else:
			context = {
				'error': "You don't have access to this question set",
				'title':'Rules',
				'firstname':request.user.first_name,
				'qgroup': qgroup,
				'qset':qset,
			}
			return render(request,'rules_iom.html', context)
	if qgroup=='MOE':
		if len(request.user.userquestionset_set.filter(qgroup='IOE',questionset=qset))>0 or qset==str(150):
			context={
				'title':'Rules',
				'firstname':request.user.first_name,
				'qgroup': qgroup,
				'qset':qset,

			}
			return render(request,'rules_moe.html', context)
		else:
			context = {
				'error': "You don't have access to this question set",
				'title':'Rules',
				'firstname':request.user.first_name,
				'qgroup': qgroup,
				'qset':qset,
			}
			return render(request,'rules_moe.html', context)


def iomstart(request):
	news = News.objects.filter(faculty__exact='IOM').order_by('-publishDate')[:5]
	context = {
		'title':'IOM Start',
		'news':news
	}
	return render(request, 'iom_start.html', context)

def ioestart(request):
	news = News.objects.filter(faculty__exact='IOE').order_by('-publishDate')[:5]
	context = {
		'title':'IOE Start',
		'news':news
	}
	return render(request, 'ioe_start.html', context)

def moestart(request):
	news = News.objects.filter(faculty__exact='MOE').order_by('-publishDate')[:5]
	context = {
		'title':'IOE Start',
		'news':news
	}
	return render(request, 'moe_start.html', context)

def ioesyllabus(request):
	context = {
	
	}
	return render(request, 'syllabus_ioe.html', context)

def iomsyllabus(request):
	context = {

	}
	return render(request, 'syllabus_iom.html', context)
def moesyllabus(request):
	context = {

	}
	return render(request, 'syllabus_moe.html', context)

def forgotpassword(request):
	if request.method == 'POST':
		# print request.POST['email']
		try:
			user = User.objects.get(email=request.POST['email'])
			if user != None:
				key = str(int(random.random()*100000000))
				message='<h1>Password Change Key</h1><br/>As you had requested for changing password your key is here: <br/><b>'+key+'</b>'
				send_mail('Notification: Your password change key is here', '',
	                'someone@email.com', [request.POST['email'],], fail_silently=False, html_message=message)
				passchg = PassChgKey.objects.create(key=key, email=request.POST['email'])
				passchg.save()
				return redirect(reverse('recoverpassword'))
			else:
				context = {
					'error': 'Email does not exist. Please Provide a valid email.'
				}
				return render(request, 'password_forgot.html', context)
		except Exception as e:
			context = {
					'error': 'Email does not exist. Please Provide a valid email.'
				}
			return render(request, 'password_forgot.html', context)
	return render(request, 'password_forgot.html')

def recoverpassword(request):
	if request.method == 'POST':
		try:
			key = PassChgKey.objects.get(key=request.POST['key'])
			if key != None:
				request.session['key'] = key
				return redirect(reverse('changepassword'))
			else:
				context = {
					'error': 'Incorrect key'
				}
				return render(request, 'password_recover.html', context)
		except Exception as e:
			context = {
					'error': 'Incorrect key'
				}
			return render(request, 'password_recover.html', context)
	return render(request, 'password_recover.html')

def changepassword(request):
	if request.session['key']:
		if request.method == 'POST':
			password1 = request.POST['password1']
			password2 = request.POST['password2']
			if password1 == password2:
				user = User.objects.get(email= request.session['key'].email)
				user.set_password(password1)
				user.save()
				request.session['key']=None
				return redirect(reverse('login'))
			else:
				context={
					'error': 'Password don\'t match'
				}
				return render(request,'password_change.html',context)
		return render(request,'password_change.html')
	else:
		return redirect(reverse('recoverpassword'))

#######################--api--#################
@csrf_exempt
def api_register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		password = request.POST['password']
		college = request.POST['college']
		faculty = request.POST['faculty']
		phone = request.POST['contact']
		test_email = None
		test_username = None
		try :
			test_email = User.objects.get(email=email)
		except Exception as e:
			pass
		if test_email != None:
			return HttpResponse('224')
		try :
			test_username = User.objects.get(username=username)
		except Exception as e:
			pass
		if test_username != None:
			return HttpResponse('225')
		user = User(username=username,email=email,first_name=firstname,last_name=lastname)
		user.set_password(password)
		user.save()
		userprofile = UserProfile(user=user,college=college,faculty=faculty,phone=phone)
		userprofile.save()
		return HttpResponse('226')
	else:
		return HttpResponse('GFY')
@csrf_exempt
def api_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# print request.META['HTTP_USERNAME']
		# print request.META['HTTP_PASSWORD']
		if '@' in username:
			try:
				username = User.objects.get(email=username).username
			except Exception as e:
				pass
			
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				return HttpResponse('226')
			else :
				return HttpResponse('225')
		else:
			return HttpResponse('224')
	else:
		return HttpResponse('GFY')

def api_dashboard(request):
	username = request.META['HTTP_USERNAME']
	password = request.META['HTTP_PASSWORD']

	if '@' in username:
		try:
			username = User.objects.get(email=username).username
		except Exception as e:
			pass
	user = authenticate(username=username, password=password)
	if user:
		if user.is_active:
			ioe_set = []
			iom_set = []
			moe_set = []
			ioe_questionset = user.userquestionset_set.filter(qgroup='IOE').order_by('questionset')
			iom_questionset = user.userquestionset_set.filter(qgroup='IOM').order_by('questionset')
			moe_questionset = user.userquestionset_set.filter(qgroup='MOE').order_by('questionset')
			for qset in ioe_questionset:
				ioe_set.append({'questionset':qset.questionset,'score':qset.score})
			for qset in iom_questionset:
				iom_set.append({'questionset':qset.questionset,'score':qset.score})
			for qset in moe_questionset:
				moe_set.append({'questionset':qset.questionset,'score':qset.score})
			question_sets = {'ioe_set':ioe_set,'iom_set':iom_set,'moe_set':moe_set}
			question_sets = json.dumps(question_sets)
			return HttpResponse(question_sets)

		else:
			return HttpResponse("224")
	else:
		return HttpResponse("224")


def api_questions(request,qgroup,qset):
	username = request.META['HTTP_USERNAME']
	password = request.META['HTTP_PASSWORD']

	if '@' in username:
		try:
			username = User.objects.get(email=username).username
		except Exception as e:
			pass
		
	user = authenticate(username=username,password=password)
	if user:
		if user.is_active:
			if qgroup=='ioe':
				questions = QuestionIOE.objects.filter(questionset=qset).order_by('questionno')[:5]
				# questionno = serializers.serialize("json", questions, fields=('question',))
				question_set = []
				# print questionno
				
				for question in questions:
					answers = question.answerioe_set.all()
					answer_set=[]
					# answer = serializers.serialize("json", answers, fields=('answer','value'))
					for answer in answers:
						answer_set.append({'answer':answer.answer,'choice':answer.choice})
					question_set.append({'question':question.question,'canswer':question.answer,'hint':question.hint,'answer':answer_set})
				print question_set
				return HttpResponse(json.dumps(question_set))
			elif qgroup=='iom':
				return HttpResponse("Not done yet")
			elif qgroup=='moe':
				return HttpResponse("Not done yet")
		else :
			return HttpResponse('GFY')
	else:
		return HttpResponse('GFY')

@csrf_exempt
def api_result(request,qgroup,qset):
	username = request.META['HTTP_USERNAME']
	password = request.META['HTTP_PASSWORD']

	if '@' in username:
		try:
			username = User.objects.get(email=username).username
		except Exception as e:
			pass
		
	user = authenticate(username=username,password=password)
	if user:
		if user.is_active:
			if request.method == 'POST':
				userqset = UserQuestionSet.objects.get(user=user,qgroup=qgroup.upper(),questionset=qset)
				score = request.POST['score']
				userqset.score = score
				userqset.save()
				return HttpResponse('sucess, Your score is: '+score)
			else:
				return HttpResponse('GFY')


		else :
			return HttpResponse('GFY')
	else:
		return HttpResponse('GFY')

@csrf_exempt
def api_forgotpassword(request):
	if request.method == 'POST':
		# print request.POST['email']
		try:
			user = User.objects.get(email=request.POST['email'])
			if user != None:
				key = str(int(random.random()*100000000))
				message='<h1>Password Change Key</h1><br/>As you had requested for changing password your key is here: <br/><b>'+key+'</b>'
				send_mail('Notification: Your password change key is here', '',
	                'someone@email.com', [request.POST['email'],], fail_silently=False, html_message=message)
				passchg = PassChgKey.objects.create(key=key, email=request.POST['email'])
				passchg.save()
				print user
				return HttpResponse('226')
			else:
				return HttpResponse('224')
		except Exception as e:
			return HttpResponse('224')
	return HttpResponse('GFY')
@csrf_exempt
def api_recoverpassword(request):
	if request.method == 'POST':
		try:
			key = PassChgKey.objects.get(key=request.POST['key'])
			if key != None:
				response = {'code':'226','email':key.email}
				response = json.dumps(response)
				return HttpResponse(response)
			else:
				return HttpResponse('224')
		except Exception as e:
			return HttpResponse('224')
	return HttpResponse('GFY')
@csrf_exempt
def api_changepassword(request):
	email = request.META['HTTP_EMAIL']
	if request.method == 'POST':
		password = request.POST['password']
		user = User.objects.get(email= email)
		user.set_password(password)
		user.save()
		return HttpResponse('226')
	else:
		return HttpResponse('GFY')




# calling function to delete the password change keys
import threading
from datetime import datetime

def removekey():
	PassChgKey.objects.filter(expiry__lt=datetime.now()).delete()
	threading.Timer(60, removekey).start()

removekey()

