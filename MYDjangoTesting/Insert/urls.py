from django.conf.urls import patterns, url

from Insert import views


urlpatterns = patterns('',	
	url(r'^firstpageRequest', views.firstpageRequest, name='firstpageRequest'),
	url(r'^firstpage', views.firstpage, name='firstpage'),
		
)