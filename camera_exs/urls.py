from django.urls import path
from .views import *

urlpatterns = [
    path('cam/', index),
    path('/camera', livefe, name="live_camera"),
    ]