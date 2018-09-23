from django.contrib import admin
from django.urls import path, include
from upstox_auth import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('redirect/', views.redirect, name='redirect'),
    path('readaccesstoken', views.readaccesstoken, name='readaccesstoken')
]
