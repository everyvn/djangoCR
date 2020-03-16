from django import forms
from .models import Book, Comment

class PostForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'contents', 'price', 'rating', 'created_date')

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)