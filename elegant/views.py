from django.shortcuts import render
from elegant.forms import PostProcedure

def client_list(request):
    return render(request, 'elegant/base.html')

def procedure(request):
    procedures = PostProcedure
    return render(request, 'elegant/procedure.html', {'procedures': procedures})
