from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin #Админка 


from . import views


urlpatterns = [
	url(r'^admin', admin.site.urls), # Админка
	url(r'^createacount$', views.createAcount), # Регистрация
	url(r'^index$', views.index), # Регистрация
	url(r'^createacount', views.createAcount), # Регистрация
	url(r'^content', views.content), #контент
	url(r'^test', views.test), #контент
	url(r'^rezultat', views.rezultat), #контент
	url(r'^fullInformation', views.fullInformation), #контент
	url(r'^adminTest', views.adminTest), #контент

	url(r'^', views.login), 
]
