from django.shortcuts import render
from .models import Salate

# Create your views here.
def salate(request):
    salate = Salate.objects.all()
    return render(request, 'salate.html', {"salate":salate})