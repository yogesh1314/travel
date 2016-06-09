from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.base, name='destination'),
	url(r'^(?P<pk>[0-9]+)/$',views.destination, name='destination-overview'),
	url(r'^(?P<pk>[0-9]+)/attractions/$',views.destination, name='destination-attractions'),
	url(r'^(?P<pk>[0-9]+)/musteat/$',views.destination, name='destination-musteat'),
	url(r'^(?P<pk>[0-9]+)/mustbuy/$',views.destination, name='destination-mustbuy'),
	url(r'^(?P<pk>[0-9]+)/whentovisit/$',views.destination, name='destination-whentovisit'),
	url(r'^(?P<pk>[0-9]+)/waystoreach/$',views.destination, name='destination-waystoreach'),
	url(r'^(?P<pk>[0-9]+)/shoppingplaces/$',views.destination, name='destination-shoppingplaces'),
	url(r'^(?P<pk>[0-9]+)/itinerary/$',views.destination, name='destination-itinerary'),
	url(r'^(?P<pk>[0-9]+)/thingstodo/$',views.destination, name='destination-things'),
]