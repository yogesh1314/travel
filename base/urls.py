from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.home, name='home'),
	url(r'^contact/$',views.contact, name='contact'),
	url(r'^contactus/$',views.contactus, name='contactus'),
	url(r'^search/$',views.search, name='search'),
]