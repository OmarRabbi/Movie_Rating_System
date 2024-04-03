from django.db import models
from main.models import Movie, UserProfile

# Create your models here.
class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.user.user.first_name} rated {self.movie.name} {self.rating}"