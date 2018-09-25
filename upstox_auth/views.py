import os
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from upstox_api import api
from django.http import Http404
from django.contrib.auth import authenticate, logout, login
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
    context = {"alert_flag": alert_flag, "alert_text": alert_text, "is_auth": request.user.is_authenticated}

    return render(request, 'upstox_auth/index.html', context=context)


def login_upstox(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("{}?alert=unauthorized".format(reverse('djangologin')))
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    s = api.Session(API_KEY)
    s.set_api_secret (API_SECRET)
    url = request.build_absolute_uri(reverse('redirect'))
    s.set_redirect_uri(url)
    return HttpResponseRedirect(s.get_login_url())

def djangologin(request):
    alert = request.GET.get('alert', False)
    alert_text =""
    if alert == "wrongpassword":
        alert_text = "Wrong username or password"
    elif alert == "loggedout":
        alert_text = "Logged out successfully"
    elif alert == "unauthorized":
        alert_text = "Please login to access this resource"
    context = {"alert_flag": alert , "alert_text": alert_text}
    return render(request, 'upstox_auth/djangologin.html', context=context)

def djangologinsubmit(request):
    userid = request.POST.get('userid')
    password = request.POST.get('password')
    user = authenticate(username=userid, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponseRedirect("{}?alert=wrongpassword".format(reverse('djangologin')))

def djangologout(request):
    logout(request)
    return HttpResponseRedirect("{}?alert=loggedout".format(reverse('djangologin')))

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
    if not request.user.is_authenticated:
        print("Loggedin")
        return HttpResponseRedirect("{}?alert=unauthorized".format(reverse('djangologin')))
    else:
        print("Not authenticated")
    code = dotenv.get_key(dotenv.find_dotenv(), 'ACCESS_TOKEN')
    context = {'accesstoken': code}
    return render(request, 'upstox_auth/tokendisplay.html', context=context)
