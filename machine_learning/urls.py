from django.urls import path
from . import views

urlpatterns = [
    path('machine/learning/', views.machine_learning),
    path('random/forest/', views.random_forest),
    path('knn/', views.knn),
    path('dt/', views.dt),
]
