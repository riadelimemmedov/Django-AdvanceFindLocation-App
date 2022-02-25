from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

#!Measurement Model
class Measurement(models.Model):
    location = models.CharField(max_length=200)#yeni oldugum yer
    destination = models.CharField(max_length=200)#yeni gedeceyim yer
    distance = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"
    
    
    