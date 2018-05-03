from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin #Админка 


from . import views


urlpatterns = [
	url(r'^admin', admin.site.urls), # Админка
	url(r'^createacount/$', views.createAcount), # Регистрация
	url(r'^login/$', views.login), # Регистрация
	url(r'^logout/$',            views.logout),         # Выход из учетной записи
	url(r'^index$', views.index), # Регистрация
	url(r'^content', views.content), #контент
	url(r'^test', views.test), #контент
	url(r'^rezultat', views.rezultat), #контент
	url(r'^fullInformation', views.fullInformation), #контент
	url(r'^adminTest', views.adminTest), #контент
	url(r'^saveTest/$', views.saveTest), #контент

	url(r'^', views.main), 
]
