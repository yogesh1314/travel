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

def destination_attraction(request, pk):
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
	return render(request, 'destination-attractions.html',data)

def destination_waytoreach(request, pk):
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
	return render(request, 'destination-waytoreach.html',data)


def destination_things(request, pk):
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
	return render(request, 'destination-things.html',data)

def destination_musteat(request, pk):
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
	return render(request, 'destination-musteat.html',data)

def destination_mustbuy(request, pk):
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
	return render(request, 'destination-mustbuy.html',data)

def destination_shoppingplaces(request, pk):
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
	return render(request, 'destination-shoppingplaces.html',data)

def destination_whentovisit(request, pk):
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
	print(data)
	return render(request, 'destination-whentovisit.html',data)

def destination_itinerary(request, pk):
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
	
	return render(request, 'destination-itinerary.html',data)
