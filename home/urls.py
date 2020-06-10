from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.loginpage, name='login'), 
    path('logout/', views.logout_user, name='logout'),
]
