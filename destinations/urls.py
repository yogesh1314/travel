from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.base, name='destination'),
	url(r'indian_destinations$',views.indian_locations, name='indian_destination'),
	url(r'international_destinations$',views.international_locations, name='international_destination'),
	url(r'asian_destinations$',views.asian_locations, name='asian_destination'),
	url(r'african_destinations$',views.african_locations, name='african_destination'),
	url(r'american_destinations$',views.american_locations, name='american_destination'),
	url(r'european_destinations$',views.european_locations, name='european_destination'),
	url(r'australian_destinations$',views.australian_locations, name='australian_destination'),
	url(r'destinations_top_searched$',views.top_searched, name='top_searched_destination'),
	url(r'^(?P<pk>[0-9]+)/$',views.destination, name='destination-overview'),
	url(r'^(?P<pk>[0-9]+)/attractions/$',views.destination_attraction, name='destination-attractions'),
	url(r'^(?P<pk>[0-9]+)/musteat/$',views.destination_musteat, name='destination-musteat'),
	url(r'^(?P<pk>[0-9]+)/mustbuy/$',views.destination_mustbuy, name='destination-mustbuy'),
	url(r'^(?P<pk>[0-9]+)/whentovisit/$',views.destination_whentovisit, name='destination-whentovisit'),
	url(r'^(?P<pk>[0-9]+)/waystoreach/$',views.destination_waytoreach, name='destination-waystoreach'),
	url(r'^(?P<pk>[0-9]+)/shoppingplaces/$',views.destination_shoppingplaces, name='destination-shoppingplaces'),
	url(r'^(?P<pk>[0-9]+)/itinerary/$',views.destination_itinerary, name='destination-itinerary'),
	url(r'^(?P<pk>[0-9]+)/thingstodo/$',views.destination_things, name='destination-things'),
]
