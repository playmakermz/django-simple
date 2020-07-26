from django.shortcuts import render,redirect
from .models import *
from .forms import *


def home(request):
    note = Note.objects.all()
    note = len(note)
    form = NoteForm()

    if request.method == 'POST':
        ab = Note(title=request.POST['title'], suara= note)
        ab.save()

    main = {
        'note':note,
        'form':form,
    }
    return render(request, 'voting/home.html', main)
            