from django.shortcuts import render
from .models import Project
from django.http import HttpResponse



# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def set_cookie(request):
    response = HttpResponse("Kolačić je postavljen!")
    response.set_cookie('cookie_name', 'vrednost_kolacica', max_age=365*24*60*60)  # Postavite trajanje kolačića na 1 godinu
    return response

def cookie_policy(request):
    # Dodajte kod za prikaz HTML stranice sa politikom kolačića
    return render(request, 'portfolio/cookie.html')
