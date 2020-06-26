from django.shortcuts import render
from .models import *
from .forms import *
from .filters import OrderFilter

def home(request):
    note = Note.objects.all()
    
    myfilter = OrderFilter()
    if request.method == 'POST':
        myfilter = OrderFilter(request.POST, queryset=note)
        #form = NoteForm(request.POST('title'))
        note = myfilter.qs 
       

    main = {
        'note':note,
        #'form':form,
        'myfilter':myfilter,
    }
    return render(request, 'home.html', main)
# Create your views here.
