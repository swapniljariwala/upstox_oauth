from django.contrib import admin
from django.urls import path, include
from upstox import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('redirect/', views.redirect, name='redirect')
]
