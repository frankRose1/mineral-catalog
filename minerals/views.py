from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Mineral

# Create your views here.


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, mineral_id):
    mineral = get_object_or_404(Mineral, pk=mineral_id)
    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})


def search(request):
    term = request.GET.get('query')
    minerals = Mineral.objects.filter(
      Q(name__icontains=term)
    )
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})