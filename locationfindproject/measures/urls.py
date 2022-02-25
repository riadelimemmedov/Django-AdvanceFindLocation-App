from django.urls import path
from .views import *

app_name='measures'

urlpatterns = [
    path('',calculate_distance_view,name='calculate_distance_view'),
]