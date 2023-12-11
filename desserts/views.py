from django.shortcuts import render
from .models import Desserts

# Create your views here.
def desserts(request):
    desserts = Desserts.objects.all()
    return render(request, 'desserts.html', {"desserts": desserts})