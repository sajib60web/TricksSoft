from django.urls import path
from . import views

urlpatterns = [
    path('deep/learning', views.deep_learning),
]
