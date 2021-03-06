from django.shortcuts import render, get_object_or_404
from elegant.forms import PostProcedure
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
    data = Price.objects.select_related('category')

    return render(request, 'elegant/price.html',
                  dict(data=data))


def news_detail(request, pk):
    post = get_object_or_404(News, pk=pk)

    return render(request, 'elegant/news_detail.html', {'post': post})


def news(request):
    posts = News.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'elegant/news.html',  {'posts': posts})


def news_sale(request):
    # if request.GET.get('news_sale'):
    posts = News.objects.filter(section__name='Sale')

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'elegant/news.html',
                  dict(posts=posts))


def news_stock(request):
    posts = News.objects.filter(section__name='Акції')

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'elegant/news.html',
                  dict(posts=posts))


def news_novelty(request):
    posts = News.objects.filter(section__name='Новини')

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'elegant/news.html',
                  dict(posts=posts))


def news_care(request):
    posts = News.objects.filter(section__name='Догляд')

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'elegant/news.html',
                  dict(posts=posts))


def contact(request):
    return render(request, 'elegant/contact.html')
