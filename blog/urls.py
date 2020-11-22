from django.urls import path
from .views import hola

urlpatterns = [
    path('hola-mundo/', hola, name="hola"),
]
