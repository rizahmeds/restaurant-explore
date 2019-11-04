from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from restaurants.models import Restaurants

# Create your views here.
class RestaurantList(ListView):
    model = Restaurants
