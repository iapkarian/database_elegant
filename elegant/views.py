from django.shortcuts import render
from django.utils import timezone
from .models import Procedure

def client_list(request):
    return render(request, 'elegant/client_list.html', {})
