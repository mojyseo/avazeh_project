from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField()
    author = models.CharField(max_length=120)
    categories = models.CharField(default="avazeh", max_length=255)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    category = models.CharField(max_length=200)
    link = models.CharField(max_length=255, default="#!")

    def __str__(self):
        return self.category
    