# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Restaurants(models.Model):
    restaurant_id = models.TextField(db_column='Restaurant ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    restaurant_name = models.TextField(db_column='Restaurant Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cuisines = models.TextField(db_column='Cuisines', blank=True, null=True)  # Field name made lowercase.
    average_cost_for_two = models.TextField(db_column='Average Cost for two', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency = models.TextField(db_column='Currency', blank=True, null=True)  # Field name made lowercase.
    has_table_booking = models.TextField(db_column='Has Table booking', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    has_online_delivery = models.TextField(db_column='Has Online delivery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aggregate_rating = models.TextField(db_column='Aggregate rating', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rating_color = models.TextField(db_column='Rating color', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rating_text = models.TextField(db_column='Rating text', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    votes = models.TextField(db_column='Votes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restaurants'


class RestaurantsLocation(models.Model):
    restaurant_id = models.ForeignKey(Restaurants, on_delete=models.CASCADE)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_code = models.TextField(db_column='Country Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    locality = models.TextField(db_column='Locality', blank=True, null=True)  # Field name made lowercase.
    locality_verbose = models.TextField(db_column='Locality Verbose', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    longitude = models.TextField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restaurants_location'
