from django.urls import path
from .views import rate_movie

app_name = 'rating'
urlpatterns = [
    path('rate-movie/<int:movie_id>/', rate_movie, name='rate_movie'),]