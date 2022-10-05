from datetime import date
from django import forms
from django.forms import ModelForm
from .models import Book


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']


class AuthorsForm(forms.Form):
    """
    Class for authors form
    """
    first_name = forms.CharField(label='Author first name')
    last_name = forms.CharField(label='Author last name')
    date_of_birth = forms.DateField(label='Date of birth', initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_of_death = forms.DateField(label='Date of death', initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
