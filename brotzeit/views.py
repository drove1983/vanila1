from django.shortcuts import render
from .models import Brotzeit

# Create your views here.
def brotzeit(request):
    brotzeit = Brotzeit.objects.all()
    return render(request, 'brotzeit.html', {"brotzeit": brotzeit})
