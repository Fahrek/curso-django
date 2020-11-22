from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="blog"),
    path('post/crear', crear_post, name="crear_post"),
]
