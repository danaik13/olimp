from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import *

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
				password = passwordField,
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
			error = ' Логин или пародб не совподает'
			return render(request,'login.html', {'errorLogin':error})
		return redirect("/index")

def logout(request):
    request.session.flush()
    return redirect("/")

def index(request):
	if connect(request):
		return render(request, "index.html")
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


def fullInformation(request):
	if connect(request):
		return render(request, "fullInformation.html")
	return redirect("/")

def adminTest(request):
	if connect(request):

		return render(request, "adminTest.html")

	return redirect("/")
	
def content(request):
	if connect(request):
		return render(request, "content.html")
	return redirect("/")
	
def test(request):
	if connect(request):
		return render(request, "test.html")
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
