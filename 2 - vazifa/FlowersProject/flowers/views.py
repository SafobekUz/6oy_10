from django.shortcuts import render, get_object_or_404, redirect
from .models import Tur, Gul

def update_tur(request, tur_id):
    tur = get_object_or_404(Tur, id=tur_id)
    if request.method == 'POST':
        tur.name = request.POST.get('name', tur.name)
        tur.save()
        return redirect('tur_detail', tur_id=tur.id)
    return render(request, 'update_tur.html', {'tur': tur})


def update_gul(request, gul_id):
    gul = get_object_or_404(Gul, id=gul_id)
    if request.method == 'POST':
        gul.name = request.POST.get('name', gul.name)
        gul.color = request.POST.get('color', gul.color)
        gul.save()
        return redirect('gul_detail', gul_id=gul.id)
    return render(request, 'update_gul.html', {'gul': gul})
