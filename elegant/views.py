from django.shortcuts import render
from elegant.forms import PostProcedure
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from elegant.utils import check_permission
from .models import News
from elegant.models import Price


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
    data_shug = Price.objects.filter(category__category='Шугарiнг')
    data_face = Price.objects.filter(category__category='Косметологiя обличчя')
    data_body = Price.objects.filter(category__category='Косметологiя тiла')

    return render(request, 'elegant/price.html',
                  dict(data_shug=data_shug, data_face=data_face, data_body=data_body))


def news(request):
    posts = News.objects.all()

    return render(request, 'elegant/news.html',
                  dict(posts=posts))


def news_sale(request):
    posts = News.objects.filter(section__name='Sale')

    return render(request, 'elegant/news.html',
                  dict(posts=posts))


def news_stock(request):
    posts = News.objects.filter(section__name='Акції')

    return render(request, 'elegant/news.html',
                  dict(posts=posts))


def news_novelty(request):
    posts = News.objects.filter(section__name='Новини')

    return render(request, 'elegant/news.html',
                  dict(posts=posts))


def news_care(request):
    posts = News.objects.filter(section__name='Догляд')

    return render(request, 'elegant/news.html',
                  dict(posts=posts))


def post(request):
    posts = News.objects.filter(request.GET)

    if request.method == 'GET':
        if "post_print" in request.GET:
            pass

    return render(request, 'elegant/news.html', dict(posts=posts))


def comments(request):
    return render(request, 'elegant/comments.html')


def contact(request):
    return render(request, 'elegant/contact.html')
