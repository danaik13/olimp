from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
import json
import hashlib
# Create your views here.

def connect(request):
	try:
		user = User.objects.get(login=request.session['login'])
		print("connect True")
		return True
	except:
		print("connect False")
		return False

def main(request):
	if connect(request):
		return redirect("/index")

	return render(request, "login.html")

def createAcount(request):
	if request.method == 'GET':
		nameField = request.GET['nameField']
		lastField = request.GET['lastField']
		loginField = request.GET['loginField']
		emailField = request.GET['emailField']
		passwordField = request.GET['passwordField']
		passwordTwoField = request.GET['passwordTwoField']
		
		if passwordField == passwordTwoField:
			createAcount = User.objects.create(
				name = nameField,
				lastname = lastField,
				login = loginField,
				email = emailField,
				password = hashlib.md5(passwordField.encode('utf-8')).hexdigest(),
			)
		else:
			error = ' Пароли не совподают'
			return render(request,'login.html', {'errorPassword':error} )
	return redirect("/index")

def login(request):
	if request.method == 'GET':
		inputLogin = request.GET['inputLogin']
		inputPassword = request.GET['inputPassword']
		try:
			user = User.objects.get(login=inputLogin)
			if hashlib.md5(inputPassword.encode('utf-8')).hexdigest() == user.password:
				request.session['login'] = inputLogin
			else:
				error = ' Логин или пароль не совподает'
				return render(request,'login.html', {'errorLogin':error})
		except:  
			error = ' Логин или пароль не совподает'
			return render(request,'login.html', {'errorLogin':error})
		return redirect("/index")

def logout(request):
    request.session.flush()
    return redirect("/")

def index(request):
	if connect(request):
		context = {
			'login' : User.objects.get(login=request.session['login']),
			'tests' : Test.objects.all(),
		}
		return render(request, "index.html", context)

	return redirect("/")

def lichcab(request):
	if connect(request):
		return render(request, "lichCab.html")
	return redirect("/")


def rezultat(request):
	if connect(request):
		return render(request, "rezultat.html")
	return redirect("/")

def saveTest(request):
	if request.method == 'GET':
		nameField = request.GET['nameField']
		timeField = request.GET['timeField']
		categoryField = request.GET['categoryField']
		shortInfoField = request.GET['shortInfoField']
		fullInfoField = request.GET['fullInfoField']

		print(nameField)
	return redirect("/")


def fullInformation(request,test_id):
	if connect(request):
		test = Test.objects.get(id=test_id)
		return render(request, "fullInformation.html", {'test':test})
	return redirect("/")

def adminTest(request):
	if connect(request):
		return render(request, "adminTest.html")

	return redirect("/")
	
def content(request):
	if connect(request):
		return render(request, "content.html")
	return redirect("/")

def do_login(login, password):
	try:
		user = User.objects.get(login=login)
	except User.DoesNotExist:
		return None
	session = Session()
	session.key = generate_long_random_key()
	session.user = user
	session.expires = datetime.now() + timedelta(days=5)
	session.save()
	return session.key

def startTest(request, test_id):
	createStartTest = StartTest.objects.create(
		timeStartTest = datetime.now(),
		test = Test.objects.get(id=test_id),
		user = User.objects.get(login=request.session['login']),
		rezult = 0,
	)
	return redirect("/page/1/")

def answer(request):
	if connect(request):
		if request.method == 'GET':
			ajax_quetion = request.GET['quetion']
			ajax_answer = request.GET['answer']
			data  = json.loads(ajax_answer)
			
			user = User.objects.get(login=request.session['login'])
			startTest = StartTest.objects.filter(user = user).last()
			idQuestion = TextQuestion.objects.get(textQuestion = ajax_quetion, test = startTest.test)
			

			boolean = False
			if idQuestion.typeQuestion == "radio":
				if str(data)[2:-2] == Question.objects.get(question=idQuestion, boolean=True, test = startTest.test).answer:
					startTest.rezult += 1
					startTest.save()
					boolean = True
				
				createAnswer = Answer.objects.create(
					#idQuestion = idQuestion,
					boolean = boolean,
					timeAnswer = datetime.now(), 
					startTest = StartTest.objects.filter(user = user).last(),
				)
			
			"""	
			
			
			print("--------------")
			print(idQuestion)
			print("--------------")
			#for ans in data:
				#print(ans)
			"""



		return render(request, "test.html")
	return redirect("/")

def test(request, page_number=1):
	if connect(request):

		#kek = Answer.objects.all()
		#kek.delete()
		
		user = User.objects.get(login=request.session['login'])
		lastData = StartTest.objects.filter(user = user).last()
		test_id = Test.objects.get(id=lastData.test.id)
		#test_id = Test.objects.get(id=1)
		textQuestion=TextQuestion.objects.filter(test=test_id)
		
		columl_qwestion = 1
		qwestions_page = Paginator(textQuestion, columl_qwestion)
		temp=[]
		for tq in textQuestion:
			temp.append(Question.objects.filter(question=tq))
		answer_page = Paginator(temp, columl_qwestion)

		context={
		         'qwestions':qwestions_page.page(page_number),
		         'answers':answer_page.page(page_number),
		}
		return render_to_response('test.html',context)
	return redirect("/")

