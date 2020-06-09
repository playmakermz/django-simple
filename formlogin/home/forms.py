from django import forms # ModelForm
from .models import *

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note 
        fields = '__all__'