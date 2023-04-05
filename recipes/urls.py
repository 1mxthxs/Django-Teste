from django.urls import path
from recipes.views import Home, contato, sobre

urlpatterns = [
    path("", Home),
    path("sobre/", sobre),
    path("contato/", contato),
]