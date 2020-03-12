from django import forms
from .models import Book

class PostForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'contents', 'price', 'rating', 'created_date')