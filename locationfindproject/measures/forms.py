from pyexpat import model
from django import forms
from .models import *

class MeasurementsModelForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['destination']
