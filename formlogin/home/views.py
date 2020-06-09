from django.shortcuts import render
from .models import *
from .forms import *

def home(request):
    note = Note.objects.all()
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid:
            form.save()

    main = {
        'note':note,
        'form':form,
    }

    return render(request, 'home.html', main)