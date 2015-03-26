from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from Insert.models import Post, Place
from Insert.populateDB import *
from django.template import loader, Context
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django import forms
import json
from django.http import HttpResponse
from django.core import serializers
from Insert.hortal import *


# Create your views here.


def firstpage(request):
	return render_to_response('index/index.html')

def firstpageRequest(request):
	print "this is from firstpageRequest"
	val = ""
	if request.method == 'GET':
		print "true"
		# for hasib, use as many fields in the input form and write respective codes
		# like
		#  val = request.GET.get('**YOUR DEFINED PARAMETER**', '')
		#  and than print it or append with HttpResponse(val)
		val = request.GET.get('query', '')
		print val		
	return HttpResponse("This is what you typed : " + str(val))
