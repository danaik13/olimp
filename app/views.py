from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.



def main(request):
        return HttpResponse(render_to_string('index.html'))