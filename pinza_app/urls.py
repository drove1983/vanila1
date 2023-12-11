from django.urls import path
from . import views

app_name = 'pinza_app'

urlpatterns = [
    path('pinza/', views.pinza, name='pinza'),  # URL za prikazivanje video sadržaja
]