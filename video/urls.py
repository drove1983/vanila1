from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('index/', views.index, name='index'),  # URL za prikazivanje video sadržaja
]