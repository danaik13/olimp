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

	fullInfo = models.TextField(verbose_name='Полная информация', default=None)
	shortInfo = models.TextField(verbose_name='Краткая информация', default=None)
	colQuition = models.IntegerField(verbose_name='Количество вопросов', default=None)
	timeTest = models.IntegerField(verbose_name='Время на прохождение', default=None)
	author = models.ForeignKey(User,  on_delete=models.CASCADE, verbose_name='Автор', default=None)
	class Meta:
	    verbose_name_plural = "Тест"
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class TextQuestion(models.Model):
	textQuestion=models.TextField(verbose_name='Текст вопроса', default=None) 
	test=models.ForeignKey(Test,  on_delete=models.CASCADE,verbose_name='Тест', default=None)
	typeQuestion = models.CharField(max_length=10, verbose_name='Тип вопроса', default=None) 
	class Meta:
		verbose_name_plural = "Текст вопроса"
	def __str__(self):              # __unicode__ on Python 2
		return self.textQuestion

class Question(models.Model):
	question=models.ForeignKey(TextQuestion,  on_delete=models.CASCADE,verbose_name='Текст вопроса', default=None)
	answer=models.TextField(verbose_name='Ответ', default=None)
	boolean = models.BooleanField(verbose_name='Правильно', default=None) 
	test=models.ForeignKey(Test,  on_delete=models.CASCADE,verbose_name='Тест', default=None)
	class Meta:
		verbose_name_plural = "Варианты ответа"
	def __str__(self):              # __unicode__ on Python 2
		return self.answer


class StartTest(models.Model):
	timeStartTest = models.DateTimeField(verbose_name='Время начала теста ', default=None)
	timeFinishTest = models.DateTimeField(verbose_name='Время завершения теста ', default=None, null=True) 
	test = models.ForeignKey(Test,  on_delete=models.CASCADE,verbose_name='Тест', default=None) 
	rezult = models.IntegerField(verbose_name='Результат', default=0)
	user = models.ForeignKey(User,  on_delete=models.CASCADE, verbose_name='Кто проходит', default=None)
	class Meta:
		verbose_name_plural = "Старт теста"


class Answer(models.Model):
	idQuestion = models.ForeignKey(TextQuestion,  on_delete=models.CASCADE,verbose_name='id вопроса', default=None)
	boolean = models.BooleanField(verbose_name='Правильно', default=None) 
	timeAnswer = models.DateTimeField(verbose_name='Время когда ответил', default=None) 
	startTest = models.ForeignKey(StartTest,  on_delete=models.CASCADE,verbose_name='Старт_тест')
	class Meta:
		verbose_name_plural = "Ответы пользователя"

"""
class Qwestion(models.Model):
	answer=models.CharField(max_length=255, verbose_name='Вопрос', default=None) 
	qwestion1=models.CharField(max_length=255, verbose_name='Ответ1', default=None)
	qwestion2=models.CharField(max_length=255, verbose_name='Ответ2', default=None)
	qwestion3=models.CharField(max_length=255, verbose_name='Ответ3', default=None)
	qwestion4=models.CharField(max_length=255, verbose_name='Ответ4', default=None)
	class Meta:
	        verbose_name_plural = "Вопрос"
	def __str__(self):              # __unicode__ on Python 2
		return self.answer

class TestQwestion(models.Model):
	qwestion=models.CharField(max_length=255, verbose_name='Вопрос', default=None) 
	test=models.ForeignKey(Test,  on_delete=models.CASCADE,verbose_name='Тест', default=None)
	class Meta:
			verbose_name_plural = "Вопрос"
	def __str__(self):              # __unicode__ on Python 2
		return self.qwestion

class Answer(models.Model):
	"" docstring for Answer""
	answer=models.CharField(max_length=225, verbose_name='Ответ', default=None)
	flagRightOrWrongAnswer= models.BooleanField(verbose_name='Корректность_ответа',default=None)
	qwestion=models.ForeignKey(TestQwestion,  on_delete=models.CASCADE, verbose_name='Вопрос', default=None)	
	class Meta:
			verbose_name_plural = "Ответ"
	def __str__(self):              # __unicode__ on Python 2
		return self.answer		
"""