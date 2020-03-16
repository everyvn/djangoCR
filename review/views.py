from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForms, CommentForms
from .models import Book, Comment
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
    # post = Post.objects.get(pk=post_pk)
    post = get_object_or_404(Book, pk=post_pk)
    if request.method =="POST":
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            #New 함수랑 다른점
            comment.post = post
            form.save() #comment.save()도 호환 가능
        return redirect('detail', post.pk)
    else:
        form = CommentForms()

    return render(request, 'detail.html', {"post":post, "form":form})

def delete_comment(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def edit(request, post_pk):
    post = get_object_or_404(Book, pk=post_pk)

    if request.method == "POST":
        form = PostForms(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForms(instance=post)
    return render(request, 'edit.html', {'form':form})

def delete(request, post_pk):
    post = get_object_or_404(Book, pk=post_pk)
    post.delete()
    return redirect('home')