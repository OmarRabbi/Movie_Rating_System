from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add-movies/', add_movies, name='add_movies'),
    path('details/<id>', details, name='movie_details'),
    path('delete-record/<id>/', delete_movies, name='delete_movies'),
    path('edit-movies/<id>/', edit_movies, name='edit_movies'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('register/', register_page, name='register_page'),
    path('userprofile/<int:user_id>', user_profile, name='user_profile'),
]
