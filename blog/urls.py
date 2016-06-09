from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.bloghome, name = 'blog-home'),
	url(r'^add/$',views.addblog, name='blog-add'),
]