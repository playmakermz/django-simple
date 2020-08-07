from django.urls import path
from . import views

urlpatterns = [
    path('item/<str:pk>', views.item, name='item'),
    path('', views.home,name='home'),
]
