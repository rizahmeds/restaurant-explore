from django.contrib import admin
from restaurants.models import Restaurants, RestaurantsLocation
# Register your models here.

admin.site.register(Restaurants)
admin.site.register(RestaurantsLocation)
