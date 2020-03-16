from django.db import models
from django.utils import timezone

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     contents = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     def __str__(self):
#         return self.title, self.created_date

class Book(models.Model): 
    title = models.CharField(max_length=200) 
    contents = models.TextField() 
    price = models.IntegerField() 
    score=(('★☆☆☆☆','★☆☆☆☆'),('★★☆☆☆','★★☆☆☆'),('★★★☆☆','★★★☆☆'), ('★★★★☆','★★★★☆'),('★★★★★','★★★★★'))
    rating = models.CharField(max_length=5, choices = score, default = '★★★☆☆',) 
    created_date = models.DateTimeField(default = timezone.now) 
    def __str__(self): 
        return self.title

class Comment(models.Model): 
    post = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    def __str__(self): 
        return self.content