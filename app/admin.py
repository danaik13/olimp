from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login','password','name')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'user','expires')
