from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse


from exam.models import *

def home(request):
	
	context = {
		"title":"Home"
	}
	return render(request,'home.html',context)