import re
import base64,random,string
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mass_mail
from base.models import *
#from .forms import *


@require_http_methods(['GET', 'POST'])
def base(request):
	data = {}
	data['destinations'] = Destination.objects.order_by('hotcount').reverse()[:10]
	return render(request, 'desthome.html',data)	


@require_http_methods(['GET'])
def destination(request, pk):
	# pass
	data = {}
	try:
		dest = Destination.objects.get(pk=pk)
		data['destination'] = dest
	except ObjectDoesNotExist:
		return redirect('home')
	data['destimages'] = DestinationImages.objects.filter(destination = dest)
	data['attractions'] = Attractions.objects.filter(destination = dest)
	data['mustbuy'] = MustBuy.objects.filter(destination = dest)
	data['musteat'] = MustEat.objects.filter(destination = dest)
	data['things'] = Things.objects.filter(destination = dest)
	data['waystoreach'] = WaysToReach.objects.filter(destination = dest)
	data['whentovisit'] = WhenToVisit.objects.filter(destination = dest)
	data['shoppingplaces'] = ShoppingPlaces.objects.filter(destination = dest)
	data['itinerary'] = Itinerary.objects.filter(destination = dest)
	return render(request, 'destination.html',data)