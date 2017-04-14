from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from elegant.models import Price


@login_required(login_url='/')
def index(request):
    data = Price.objects.all()
    print(data)

    return render(request, 'elegant/price.html',
                  dict(data=data))
