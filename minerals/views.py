from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Mineral

# Create your views here.

def mineral_list(request):
    starts_with = request.GET.get('starts_with', None)
    group = request.GET.get('group', None)
    if group:
        minerals = Mineral.objects.filter(
          Q(group__iexact=group)
        )
    elif starts_with:
        minerals = Mineral.objects.filter(
          Q(name__istartswith=starts_with)
        )
    else:
        minerals = Mineral.objects.filter(
          Q(name__istartswith='A')
        )
    context = {
      'minerals': minerals,
      'letter': starts_with,
      'group': group
    }
    return render(request, 'minerals/mineral_list.html', context=context)


def mineral_detail(request, mineral_id):
    mineral = get_object_or_404(Mineral, pk=mineral_id)
    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})


def search(request):
    term = request.GET.get('query')
    minerals = Mineral.objects.filter(
      Q(name__icontains=term)|Q(mohs_scale_hardness__exact=term)|Q(crystal_system__icontains=term)
    )
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})

