from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.



def main(request):
	#context = {}

	return render(request, "index.html")


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
	return render(request,'login.html',{'error':error})
