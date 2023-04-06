from .models import Book
from django.forms import ModelForm
from django import forms

# Declaring the ModelForm
class EditBookForm(ModelForm):

    class Meta:
        # First specify what the model will inherit
        model = Book
        # Select the desired fields from the model
        fields = '__all__'
        # Apply the Bootstrap styling classes
        widget ={
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'isbn' : forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.TextInput(attrs={'class': 'form-control'}),
            'image' : forms.TextInput(attrs={'class': 'form-control'}),
        }