from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.title}"
    

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)












class Product(models.Model):
    name =  models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
