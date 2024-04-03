from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Movie, UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from rating.models import Rating
from django.db.models import Avg

# Create your views here.
@login_required(login_url="/login/")
def add_movies(request):
    if request.method == "POST":
        data = request.POST
        movie_name = data.get('movie_name')
        movie_description = data.get('movie_description')
        movie_director = data.get('movie_director')
        movie_cast = data.get('movie_cast')
        movie_genre = data.get('movie_genre')
        movie_rating = data.get('movie_rating')
        movie_release_date = data.get('movie_release_date')
        movie_poster = data.get('movie_poster')
        Movie.objects.create(
            name = movie_name,
            description = movie_description,
            director = movie_director,
            cast = movie_cast,
            genre = movie_genre,
            rating = movie_rating,
            release_date = movie_release_date,
            poster = movie_poster,
        )
        return redirect('/add-movies/')
    return render(request,'addmovies.html', context={'page':'add-movies', 'controller': 'Add Movie'})
@login_required(login_url="/login/")
def homepage(request):
    movies = Movie.objects.all()
    if request.GET.get('search'):
        movies = movies.filter(name__contains = request.GET.get('search'))
    context={
        'movies': movies,
        'page': 'homepage',
    }
    return render(request, 'homepage.html',context)
@login_required(login_url="/login/")
def details(request, id):
    movie = get_object_or_404(Movie, pk=id)
    ratings = Rating.objects.filter(movie=movie)
    average_rating = ratings.aggregate(avg_rating=Avg('rating'))['avg_rating']
    context={
        'movie':movie,
        'average_rating': average_rating,
        'page': 'movie-details'
    }
    return render(request,'moviedetails.html',context)
@login_required(login_url="/login/")
def edit_movies(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        movie.name = data.get('movie_name')
        movie.description = data.get('movie_description')
        movie.director = data.get('movie_director')
        movie.cast = data.get('movie_cast')
        movie.genre = data.get('movie_genre')
        movie.rating = data.get('movie_rating')
        movie.release_date = data.get('movie_release_date')
        movie.poster = data.get('movie_poster')
        movie.save()
        return redirect('movie_details', id)
    return render(request, 'addmovies.html',context={'movie': movie, 'page':'edit-movie', 'controller': 'Edit Movie'})
def delete_movies(request, id):
    movie = Movie.objects.get(id = id)
    movie.delete()
    return redirect('/')

def register_page(request):
    if request.method == 'POST':
        full_name = request.POST['first_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = full_name
        user.save()
        user_profile = UserProfile.objects.create(user=user, phone_number=phone_number)
        user_profile.save()

        messages.success(request, 'Registration successful. You can now login.')
        return redirect('/login/')
    else:
        return render(request, 'register.html')
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login/')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/login/')
    else:
        return render(request, 'login.html', context={'page': 'login'})
def logout_page(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('/login/')
def user_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user__id=user_id)
    return render(request,'userprofile.html',{'user':user_profile})