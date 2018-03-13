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
	expires = models.DateTimeField()
	class Meta:
	        verbose_name_plural = "Сессия"
	def __str__(self):              # __unicode__ on Python 2
		return self.key
