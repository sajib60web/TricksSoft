from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about_us(request):
    return HttpResponse("Welcome to About Us")