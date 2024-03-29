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
from travel import settings

@require_http_methods(['GET', 'POST'])
def home(request):
	data = {}
	images= HomeImages.objects.all()
	data={"images":images, }
	data['destination'] = Destination.objects.order_by('hotcount').reverse()[:6]
	bloglist = []
	blogs = Review.objects.filter(is_visible=True).order_by('created_on')[:12]
	for i in blogs:
		b = {}
		b['blog'] = i
		b['images'] = ReviewImages.objects.filter(review = i)
		bloglist.append(b)
	data['blogs'] = bloglist
	print(data)
	return render(request, 'home.html',data)

def contactus(request):
	data = {}
	return render(request,'contactus.html')


@require_http_methods(['GET', 'POST'])
def search(request):
	data = {}
	query = request.GET.get('search')
	data['query'] = query
	data['dest'] = Destination.objects.filter(title__icontains=query)
	data['attr'] = Attractions.objects.filter(title__icontains=query)
	data['musteat'] = MustEat.objects.filter(title__icontains=query)
	data['mustbuy'] = MustBuy.objects.filter(title__icontains=query)
	data['things'] = Things.objects.filter(title__icontains=query)
	data['shop'] = ShoppingPlaces.objects.filter(title__icontains=query)
	data['blog'] = Review.objects.filter(title__icontains=query)
	return render(request, 'base/search.html',data)
@require_http_methods(['GET', 'POST'])
def contact(request):
	data = {}
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = 'New Query in Travel Website'
			to = 'travellog101@gmail.com'
			body = 'Hello Admin, \n\nThere is new query in your travel website, as follows:\n\nName: '+str(form.cleaned_data.get('name'))+'\nEmail: '+str(form.cleaned_data.get('email'))+'\nContact Number: '+str(form.cleaned_data.get('contactno'))+'\nAbout: '+str(form.cleaned_data.get('about'))+'\nDescription: '+str(form.cleaned_data.get('description'))+'\n\nDo take appropriate action.\nThank You.'
			print (subject)
			print(body)
			try:
				send_mail(subject, body, settings.EMAIL_HOST_USER, [to,], fail_silently=False)
			except:
				pass
			return render(request, 'contact_redirect.html',data)
	data['contactform'] = form
	return render(request, 'contact.html',data)
def bad_request(request):
    return render(request,'base/err400.html',)

def permission_denied(request):
    return render(request,'base/err403.html',)

def page_not_found(request):
    return render(request,'base/err404.html',)

def server_error(request):
    return render(request,'base/err500.html',)