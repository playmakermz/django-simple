from django.shortcuts import render
from .models import *
import os

def main(request):
    note = Note.objects.all()

    if request.method == 'POST':
        title00 = request.POST['title']
        #tipe00 = request.POST['tipe']
        myfile00 = request.FILES.get('myfile')

        tipenya = myfile00.content_type
        ukurannya = myfile00.size

        data = Note(title=title00, tipe=tipenya, ukuran = ukurannya, myfile= myfile00)
        data.save()

    main = {
    'note':note,
    }
    return render(request, 'home.html', main)
# Create your views here.
