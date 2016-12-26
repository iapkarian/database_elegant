from django.shortcuts import render
from elegant.forms import PostProcedure


def client_list(request):
    return render(request, 'elegant/main.html')


def procedure(request):
    procedures = PostProcedure
    return render(request, 'elegant/procedure.html', {'procedures': procedures})


def shugaring(request):
    return render(request, 'elegant/shugaring.html')


def price(request):
    return render(request, 'elegant/price.html')


def news(request):
    return render(request, 'elegant/news.html')


def contact(request):
    return render(request, 'elegant/contact.html')
