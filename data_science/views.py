from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def data_science(request):
    return render(request, 'data_science/index.html', {})
    
