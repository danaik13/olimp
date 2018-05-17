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
    list_display = ('id', 'name', 'сategorie', 'gropUser', 'dateStart', 'fullInfo', 'shortInfo', 'colQuition', 'timeTest', 'author')

@admin.register(TextQuestion)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id','textQuestion','test','typeQuestion')


@admin.register(Question)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id','question','answer','boolean', 'test')


"""
@admin.register(Qwestion)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id','answer',	'qwestion1',	'qwestion2',	'qwestion3',	'qwestion4')

@admin.register(TestQwestion)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id','qwestion', 'test')

@admin.register(Answer)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id','answer','flagRightOrWrongAnswer','qwestion')
"""