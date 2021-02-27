from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('gallery/', gallery_v, name="gallery"), 
    path('pesanan/<str:pk>/', item_post, name="barang"),
    path('about-us/', about_usv, name="about-us")
]
