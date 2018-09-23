import os
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from upstox_api import api
from django.http import Http404
import dotenv
# Create your views here.

def home(request):
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    alert_text = "Please set up the environment. "
    alert_flag = False
    if not API_KEY:
        alert_flag = True
        alert_text = alert_text + "Could not find API KEY. "
    if not API_SECRET:
        alert_flag = True
        alert_text = alert_text + "Could not find API SECRET."
    context = {"alert_flag": alert_flag, "alert_text": alert_text}

    return render(request, 'upstox_auth/index.html', context=context)


def login(request):
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    s = api.Session(API_KEY)
    s.set_api_secret (API_SECRET)
    url = request.build_absolute_uri(reverse('redirect'))
    s.set_redirect_uri(url)
    return HttpResponseRedirect(s.get_login_url())

def redirect(request):
    code = request.GET.get('code')
    if not code:
        raise Http404("Did not receive ACCESS_TOKEN")
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    s = api.Session(API_KEY)
    s.set_api_secret (API_SECRET)
    url = request.build_absolute_uri(reverse('redirect'))
    s.set_redirect_uri(url)
    s.set_code(code)
    access_token = s.retrieve_access_token()
    print(access_token)
    dotenv.set_key(dotenv.find_dotenv(), 'ACCESS_TOKEN', access_token)
    return HttpResponseRedirect(reverse('readaccesstoken'))

def readaccesstoken(request):
    code = dotenv.get_key(dotenv.find_dotenv(), 'ACCESS_TOKEN')
    context = {'accesstoken': code}
    return render(request, 'upstox_auth/tokendisplay.html', context=context)