from django.urls import path
from . import views

urlpatterns = [
    path('data/science', views.data_science),
]
