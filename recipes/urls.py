from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home),
    path("recipe/<int:id>/", views.recipe),
    path("asdf/", views.Home),
]