from django.db import models

# Create your models here.

class user(models.Model):
	login    = models.CharField(unique=True)
	password = models.CharField()
	name     = models.CharField()
    class Meta:
        verbose_name = "Пользователь"
    def __str__(self):
        return '{}'.format(self.login)


class Session(models.Model):
	key = models.CharField(unique=True)
	user = models.ForeignKey(user)
	expires = models.DateTimeField()
	class Meta:
        verbose_name = "Сессия"
    def __str__(self):
        return '{}'.format(self.user)