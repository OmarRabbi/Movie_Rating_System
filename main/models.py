from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    director = models.CharField(max_length=200)
    cast = models.CharField(max_length=700)
    genre = models.CharField(max_length=200)
    rating = models.CharField(max_length=10)
    release_date = models.DateField()
    poster = models.URLField(max_length=1000, default=None, null=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
    