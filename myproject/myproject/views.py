
from django.shortcuts import render

def hri(request):
    return render(request, 'website/index.html')

def harry(request):
    return render(request, 'website/harry.html')

