from django.contrib import admin
from .models import *

# Register your models here.
class User(admin.ModelAdmin):
    list_display = ('id', 'login','password','name')
    
class Session(admin.ModelAdmin):
    list_display = ('id', 'key', 'user','expires')

admin.site.register(User, UserAdmin)
admin.site.register(Session, SessionAdmin)