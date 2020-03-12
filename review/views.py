from django.shortcuts import render, redirect
from .forms import PostForms
from .models import Book
# Create your views here.

def home(request):
    posts = Book.objects.all()
    return render(request, 'home.html', {'posts':posts})

def new(request):
    if request.method == "POST":
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = PostForms()
    return render(request, 'new.html', {'form':form})

def detail(request, post_pk):
    post = Book.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post': post})