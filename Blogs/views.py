from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blogs/index.html', {})
    
