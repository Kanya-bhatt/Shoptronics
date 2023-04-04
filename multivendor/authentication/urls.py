from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('index', views.home1, name = "home1"),
    path('signup', views.signup, name = "signup"),
    path('signin', views.signin, name = "signin"),
    path('signout', views.signout, name = "signout"),
    path('main', views.main, name="main")
]
