from django.urls import path
from . import views

app_name = 'hauptgerichte'

urlpatterns = [
    path('hauptgerichte/', views.hauptgerichte, name='hauptgerichte')
]