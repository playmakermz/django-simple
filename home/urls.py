from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a1/', views.p1, name='a1'),
    path('a2/', views.p2, name='a2'),
    path('a3/', views.p3, name='a3'),
    path('a4/', views.p4, name='a4'),
]
