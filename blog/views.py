import re
import base64,random,string
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mass_mail, send_mail
from .models import *
from .forms import *
from django.conf import settings

@require_http_methods(['GET', 'POST'])
def bloghome(request):
	data = {}
	bloglist = []
	blogs = Review.objects.filter(is_visible=True).order_by('created_on')
	for i in blogs:
		b = {}
		b['blog'] = i
		b['images'] = ReviewImages.objects.filter(review = i)
		bloglist.append(b)
	data['blogs'] = bloglist
	print(data)
	return render(request, 'bloghome.html',data)

@require_http_methods(['GET', 'POST'])
def addblog(request):
	data = {}
	if request.method == 'GET':
		form = AddBlogForm()
	elif request.method == 'POST':
		form = AddBlogForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	data['form'] = form
	return render(request, 'addblog.html',data)
