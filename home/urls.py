from django.urls import path
from . import views
urlpatterns = [
    path('division', views.division, name='division'),
    path('power/', views.power, name='power'),
    path('', views.home, name='home'),
]