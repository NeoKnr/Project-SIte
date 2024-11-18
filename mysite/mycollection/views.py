from django.shortcuts import render
from django.http import HttpResponse
from .models import Telephone
from django.shortcuts import get_object_or_404

def index(request):
    tel_list = Telephone.objects.all()
    context = {'tel_list': tel_list}
    return render(request, 'Telephones/index.html', context)

def detail(request, tel_id):
    t = get_object_or_404(Telephone, pk=tel_id)
    return render(request, 'Telephones/detail.html', {'telephone': t})