from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.base, name='destination'),
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