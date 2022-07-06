from django.urls import path
from . import views

urlpatterns = [
    path('machine/learning', views.machine_learning),
]
