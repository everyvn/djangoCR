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
    score = ((1,'1'),(2,'2'),(3,'3'),(4,'4'), (5,'5'))
    score = ((1,1),(2,2),(3,3),(4,4),(5,5))
    score = ((1,'☾'),(2,'☾☾'),(3,'☾☾☾'), (4,'☾☾☾☾'),(5,'☾☾☾☾☾'))
    rating = models.IntegerField()
    choices = score,
    default = 3,
    created_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.title