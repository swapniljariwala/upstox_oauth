import os
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from upstox_api import api
import dotenv
# Create your views here.

def home(request):
    return HttpResponse("hello World")


def login(request):
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('SECRET_KEY')
    s = api.Session(API_KEY)
    url = request.build_absolute_uri(reverse('redirect'))
    s.set_redirect_uri(url)
    return HttpResponseRedirect(s.get_login_url())

def redirect(request):
    code = request.GET.get('code')
    dotenv.set_key(dotenv.find_dotenv(), 'ACCESS_TOKEN', code)
    return HttpResponse(code)

