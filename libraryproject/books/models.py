from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True)
    published_date = models.DateField()
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title
    
