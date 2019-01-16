from django.shortcuts import render
from .models import Mineral

# Create your views here.


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'mineral_list.html', {'minerals': minerals})
