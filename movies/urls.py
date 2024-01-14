from django.urls import path
from . import views

# URL Configuration:
# Here, we add objects that map url endpoints or view functions
app_name = "movies"

urlpatterns = [
    path('', views.index, name = "index"), 
    path('<int:movie_id>', views.detail, name = "detail")
]