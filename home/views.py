from django.shortcuts import render, redirect
import django_filters
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import TemplateView, ListView

class OrderFilter(django_filters.FilterSet):
        name = django_filters.CharFilter(lookup_expr='iexact')
        class Meta:
            model = barang_jual
            fields = ['title']

def homepage(request):
    items = barang_jual.objects.all()
    myfilter = OrderFilter()
    if request.method == 'POST':
        myfilter = OrderFilter(request.POST, queryset=items)
        items = myfilter.qs
     
    main = {
            'items':items,
            'myfilter':myfilter,
    }
    return render(request, "homepage/index.html", main)

def gallery_v(request):
    items = gallery.objects.all()
    main = {
    'items':items,
            }
    return render(request, "gallery/index.html", main)

def item_post(request, pk):
    items = barang_jual.objects.get(id=pk)
    main = {
    'items':items,
            }
    return render(request, "pesanan/index.html", main)

def about_usv(request):
    items   = about_us.objects.all()
    main = {
            'items':items,
            }
    return render(request, "about-us/index.html",main)


    
# Create your views here.
