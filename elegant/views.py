from django.shortcuts import render
from elegant.forms import PostProcedure
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def home(request):
   context = RequestContext(request, {'request': request, 'user': request.user})
   return render_to_response('elegant/contact.html', context_instance=context)


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


def comments(request):
    return render(request, 'elegant/comments.html')


def contact(request):
    return render(request, 'elegant/contact.html')
