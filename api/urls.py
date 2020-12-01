from django.urls import path

from . import views

urlpatterns = [

    path('auth', views.auth, name='auth'),
    path('check', views.check, name='check'),
    path('user', views.user, name='user'),
]