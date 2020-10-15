from django.shortcuts import render
from .models import laptop
# Create your views here.

def product(request):
    laptops = laptop.objects.all()
    return render(request, 'index.html', {'laptops':laptops})