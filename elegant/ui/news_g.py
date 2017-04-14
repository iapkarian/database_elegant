from django.shortcuts import render

from elegant.models import News
from elegant.utils import check_permission


@check_permission('news_g')
def news_g(request):
    posts = News.objects.filter()
    return render(request, 'elegant/news.html',
                  dict(posts=posts))
