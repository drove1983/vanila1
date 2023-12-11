from django.shortcuts import render
from .models import Hauptgerichte

# Create your views here.
def hauptgerichte(requests):
    hauptgerichte = Hauptgerichte.objects.all()
    return render(requests, 'hauptgerichte.html', {"hauptgerichte":hauptgerichte})
