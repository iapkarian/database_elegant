from django.shortcuts import render

from elegant.models import Price


def index(request):
    data = Price.objects.filter(category='Шугарiнг')

    return render(request, 'elegant/template/elegant/price.html', dict(data=data))
