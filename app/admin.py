from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login','password','name', 'lastname','email')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'user','expires')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'сategorie')

@admin.register(GropUser)
class GropUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'gropUser')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'сategorie', 'gropUser', 'dateStart', 'dateEnd')