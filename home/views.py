from django.shortcuts import render
from .models import *
from .filters import OrderFilter
# Create your views here.
def home(request):
    note = Note.objects.all()
    myfilter = OrderFilter()
    if request.method == 'POST':
        myfilter = OrderFilter(request.POST, queryset=note) # pakai note
        note = myfilter.qs
        

    main = {
        'myfilter':myfilter,
        'note':note,

    }

    return render(request, 'jumbotron/index.html', main)

def item(request, pk):
    note = Note.objects.get(id=pk)

    main = {
        'note':note,
    }
    return render(request, 'sticky-footer-navbar/index.html',main)