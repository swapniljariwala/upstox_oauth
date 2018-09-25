from django.contrib import admin
from django.urls import path, include
from upstox_auth import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_upstox, name='login'),
    path('redirect/', views.redirect, name='redirect'),
    path('readaccesstoken/', views.readaccesstoken, name='readaccesstoken'),
    path('djangologin/', views.djangologin, name='djangologin'),
    path('djangologinsubmit/', views.djangologinsubmit, name='djangologinsubmit'),
    path('djangologout/', views.djangologout, name='djangologout')
    
]
