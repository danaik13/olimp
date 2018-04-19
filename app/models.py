from django.db import models

# Create your models here.
class User(models.Model):
	login    = models.CharField(max_length=255, verbose_name='Логин')
	password = models.CharField(max_length=255, verbose_name='Пароль')
	name     = models.CharField(max_length=255, verbose_name='Имя')
	
	class Meta:
	    verbose_name_plural = "Пользователь"
	def __str__(self):              # __unicode__ on Python 2
		return self.login

class Session(models.Model):
	key = models.CharField(max_length=255, verbose_name='Ключ')
	user = models.ForeignKey(User,  on_delete=models.CASCADE, verbose_name='Пользователь')
	expires = models.DateTimeField(verbose_name='Время сессии')
	class Meta:
	        verbose_name_plural = "Сессия"
	def __str__(self):              # __unicode__ on Python 2
		return self.key

class Categorie(models.Model):
	сategorie = models.CharField(max_length=255, verbose_name='Категория')
	class Meta:
	        verbose_name_plural = "Категория"
	def __str__(self):              # __unicode__ on Python 2
		return self.сategorie

class GropUser(models.Model):
	gropUser = models.CharField(max_length=255, verbose_name='Группа пользователей')
	class Meta:
	        verbose_name_plural = "Группа пользователей"
	def __str__(self):              # __unicode__ on Python 2
		return self.gropUser

class Test(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название теста') 
	сategorie = models.ForeignKey(Categorie,  on_delete=models.CASCADE, verbose_name='Категория')
	gropUser = models.ForeignKey(GropUser,  on_delete=models.CASCADE, verbose_name='Группа пользователей')
	dateStart = models.DateTimeField(verbose_name='Начало теста')
	dateEnd = models.DateTimeField(verbose_name='Окончание теста')

	class Meta:
	        verbose_name_plural = "Тест"
	def __str__(self):              # __unicode__ on Python 2
		return self.name