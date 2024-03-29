from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.
class MovieResource(ModelResource):
    class Meta: #meta data about the class MovieResource
        queryset = Movie.objects.all() # all returns a query - executed later; lazy loading
        resource_name = "movies"
        excludes= ['date_created'] 
