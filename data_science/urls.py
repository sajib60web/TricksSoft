from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_science),
]
