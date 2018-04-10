from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import *
# Create your views here.



def createAcount(request):
	if request.method == 'POST':
		login     = "dsd"#request.POST['loginField']
		password  = "a" #request.POST['passwordField']
		password2 = "a" #request.POST['passwordTwoField']
		email     = "a@wsa.ew" #request.POST['emailField']
		name     = "a" #request.POST['nameField']
		lastname  = "d" #request.POST['lastField']
		
		if password==password2:
			print("WOW! New User :3")
			"""db_create_account = User.objects.create(
				login    = login,
				password = password,
				gropUser = GropUser.object.get(id=1),
				surname  = lastname,
				email    = email,
				name     = name,         
			)
     """
	return render(request, "index.html")


def index(request):
#context = {}

	return render(request, "index.html")

def lichCab(request):
#context = {}

	return render(request, "lichCab.html")



def rezultat(request):
#context = {}

	return render(request, "rezultat.html")

def fullInformation(request):
#context = {}

	return render(request, "fullInformation.html")

def adminTest(request):
#context = {}

	return render(request, "adminTest.html")
	
def content(request):
	#context = {}

	return render(request, "content.html")
	
def test(request):
	#context = {}

	return render(request, "test.html")
	

def do_login(login, password):
	try:
		user = User.object.get(login=login)
	except User.DoesNotExist:
		return None
	session = Session()
	session.key = generate_long_random_key()
	session.user = user
	session.expires = datetime.now + timedelta(days=5)
	session.save()
	return session.key

def login(request):
	"""
	error=''
	if request.method == 'POST':
		login = request.POST.get('login')
		password = request.POST.get('password')
		url = request.POST.get('continue','/')
		sessid = do_login(login,password)
		if sessid:
			response = HttpResponseRedirect(url)
			response.set_cookie('sessid',sessid,
				domain='.site.com',httponly=True,
				expires = datetime.now()+timedelta(days=5)
			)
			return response
		else:
			error = u'Неверный логин / пароль'
			"""
	return render(request,'login.html')


"""
if password == password2:

return render(request, "login.html")
else:
return render(request, 'createAcount.html', {'error': 'Пароли не совпадают'})
"""