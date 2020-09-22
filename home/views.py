from django.shortcuts import render
from .models import *
def home(request):

    if request.method == 'POST':
        nama01 , pesanan01 = request.POST['nama'], request.POST['pesanan']
        #print(nama01, pesanan01)
        data_simpan = pesanan(nama = nama01, pesanan = pesanan01)
        data_simpan.save()

    return render(request, 'home.html')

def p1(request):
    data_client = pesanan.objects.all()

    if request.method == 'POST':
        nama01 , pesanan01 = request.POST['nama'], request.POST['pesanan']

        data_oke = acc1(nama = nama01, pesanan = pesanan01)
        data_oke.save()


    main = {
    'all_data':data_client,
    }
    return render(request, 'p1.html', main)

def p2(request):
    data_client = acc1.objects.all()

    if request.method == 'POST':
        nama01 , pesanan01 = request.POST['nama'], request.POST['pesanan']

        data_oke = acc2(nama = nama01, pesanan = pesanan01)
        data_oke.save()


    main = {
    'all_data':data_client,
    }
    return render(request, 'p1.html', main)

def p3(request):
    data_client = acc2.objects.all()

    if request.method == 'POST':
        nama01 , pesanan01 = request.POST['nama'], request.POST['pesanan']

        data_oke = acc3(nama = nama01, pesanan = pesanan01)
        data_oke.save()


    main = {
    'all_data':data_client,
    }
    return render(request, 'p1.html', main)

def p4(request):
    data_client = acc3.objects.all()

    if request.method == 'POST':
        nama01 , pesanan01 = request.POST['nama'], request.POST['pesanan']

        data_oke = acc3(nama = nama01, pesanan = pesanan01)
        data_oke.save()


    main = {
    'all_data':data_client,
    }
    return render(request, 'p1.html', main)
