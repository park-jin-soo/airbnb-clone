from django.shortcuts import render
from rooms import views as room_views

# Create your views here.


urlpatterns = [path("", room_views.all_rooms)]
