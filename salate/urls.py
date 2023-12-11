from django.urls import path
from . import views

app_name = 'salate'

urlpatterns = [
    path('salate/', views.salate, name='salate')
]