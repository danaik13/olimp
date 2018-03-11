from django.conf.urls import url
from django.contrib import admin #Админка 


from . import views


urlpatterns = [
   url(r'^admin', admin.site.urls),      # Админка
   url(r'^',      views.main), 
]
