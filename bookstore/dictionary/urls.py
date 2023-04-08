# First import is for views, HomeView and SearchView
# Second import is for path 
from . import views
from books import views as book_views
from django.urls import path

urlpatterns = [
    path('', views.homeView, name='dictionary'),
    path('search/', views.searchView, name='search'),
    path('bookstore/', book_views.home, name='home')
]