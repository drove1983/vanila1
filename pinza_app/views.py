from django.shortcuts import render
from .models import Pinza

# Create your views here.
def pinza(reguest):
    pinza = Pinza.objects.all()
    return render(reguest, 'pinza.html', {"pinza": pinza})
