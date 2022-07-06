from django.urls import path
from . import views

urlpatterns = [
    path('data/analysis', views.data_analysis),
]
