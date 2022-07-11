# path function to define each route
from django.urls import path
from . import views

# urlpatterns to hold each route
urlpatterns = [
path('', views.home, name='home'),
]