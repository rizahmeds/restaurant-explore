from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from restaurants.models import Restaurants

# Create your views here.
class RestaurantList(ListView):
    model = Restaurants
    paginate_by = 10

class RestaurantDetailView(DetailView):
    model = Restaurants
