from django.urls import path
from .import views

app_name = "brotzeit"

urlpatterns = [
    path('brotzeit/', views.brotzeit, name='brotzeit')
]