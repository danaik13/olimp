from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin #Админка 
from app import urls as app_urls

from . import views


urlpatterns = [
	url(r'^admin', admin.site.urls), # Админка
	url(r'^createacount/$', views.createAcount), # Регистрация
	url(r'^login/$', views.login), # Регистрация
	url(r'^logout/$', views.logout),         # Выход из учетной записи
	url(r'^index$', views.index), # Регистрация
	

	url(r'^fullInformation/(?P<test_id>\w)/$', views.fullInformation, name="fullInformation"),
	
	url(r'^test/(?P<test_id>\w+)/$', views.test,  name="test"), #контент
	url(r'^page/(\d+)/$', views.test),
	
	url(r'^content', views.content), #контент
	url(r'^rezultat', views.rezultat), #контент
	url(r'^adminTest', views.adminTest), #контент
	url(r'^saveTest/$', views.saveTest), #контент 
	url(r'^lichcab/$', views.lichcab), #контент

	url(r'^index/(?P<сategorie_id>\w)/$', views.showTests,  name="сategorie"), #контент




	url(r'^', views.main), 
]
