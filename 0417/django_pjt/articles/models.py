from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.title}"
    
class Person(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.id}: {self.name}"

# class Book(models.Model):
#     필드 설정

# class Library(models.Model):
#     필드 설정