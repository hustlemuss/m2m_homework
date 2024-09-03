from django.shortcuts import render

from articles.models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    tags = Tag.objects.all()
    context = {
        'object_list': articles,
        'tags': tags
    }


    return render(request, template, context)
