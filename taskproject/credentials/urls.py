from . import views
from django.urls import path
#from django.contrib import admin

urlpatterns = [

    path('register', views.register,name='register'),
    path('login',views.login, name='login'),
    path('application', views.finalmessage,name='finalmessage'),
    path('logout',views.logout,name='logout'),
    path('credentials/logout',views.logout,name='logout'),
]