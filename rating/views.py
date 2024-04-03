from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Movie
from .models import Rating
from django.contrib import messages
from django.urls import reverse

# Create your views here.
@login_required
def rate_movie(request, movie_id):
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        movie = Movie.objects.get(pk=movie_id)
        user_profile = request.user.userprofile
        
        existing_rating = Rating.objects.filter(user=user_profile, movie=movie).exists()
        if existing_rating:
            messages.warning(request, "You have already rated this movie.")
            return redirect(reverse('movie_details', kwargs={'id': movie_id}))
        else:
            rating = Rating.objects.create(user=user_profile, movie=movie, rating=rating_value)
            return redirect (reverse('movie_details', kwargs={'id': movie_id}))
    else:
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'rate_movie.html', {'movie': movie})