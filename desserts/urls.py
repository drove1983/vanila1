from django.urls import path
from . import views

app_name = 'desserts'

urlpatterns = [
    path('desserts/', views.desserts, name="desserts")
]