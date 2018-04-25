from django.db import models

# Create your models here.
class User(models.Model):
	name     = models.CharField(max_length=255, verbose_name='Имя', default=None)
	lastname     = models.CharField(max_length=255, verbose_name='Фамилия', default=None)
	login    = models.CharField(max_length=255, verbose_name='Логин', default=None)
	password = models.CharField(max_length=255, verbose_name='Пароль', default=None)
	email = models.EmailField(max_length=255, verbose_name='email', default=None)
	class Meta:
	    verbose_name_plural = "Пользователь"
	def __str__(self):              # __unicode__ on Python 2
		return self.login

class Session(models.Model):
	key = models.CharField(max_length=255, verbose_name='Ключ', default=None)
	user = models.ForeignKey(User,  on_delete=models.CASCADE, verbose_name='Пользователь', default=None)
	expires = models.DateTimeField(verbose_name='Время сессии', default=None)
	class Meta:
	        verbose_name_plural = "Сессия"
	def __str__(self):              # __unicode__ on Python 2
		return self.key

class Categorie(models.Model):
	сategorie = models.CharField(max_length=255, verbose_name='Категория', default=None)
	class Meta:
	        verbose_name_plural = "Категория"
	def __str__(self):              # __unicode__ on Python 2
		return self.сategorie

class GropUser(models.Model):
	gropUser = models.CharField(max_length=255, verbose_name='Группа пользователей', default=None)
	class Meta:
	        verbose_name_plural = "Группа пользователей"
	def __str__(self):              # __unicode__ on Python 2
		return self.gropUser

class Test(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название теста', default=None) 
	сategorie = models.ForeignKey(Categorie,  on_delete=models.CASCADE, verbose_name='Категория', default=None)
	gropUser = models.ForeignKey(GropUser,  on_delete=models.CASCADE, verbose_name='Группа пользователей', default=None)
	dateStart = models.DateTimeField(verbose_name='Начало теста', default=None)
	dateEnd = models.DateTimeField(verbose_name='Окончание теста', default=None)

	class Meta:
	        verbose_name_plural = "Тест"
	def __str__(self):              # __unicode__ on Python 2
		return self.name