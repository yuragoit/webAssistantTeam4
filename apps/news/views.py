from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import ListView
from django.core.management import call_command
from . import crawlers
from .models import News


class ViewNews(ListView):
    model = News
    context_object_name = "scrapped_news"
    queryset = model.objects.all()
    call_command("crawl")


# Create your views here.
def app_news(request):
    queryset = ViewNews.queryset
    categoryes = []
    for elem in queryset:
        if elem.category not in categoryes:
            categoryes.append(elem.category)

    context = {"news": queryset, "categoryes": categoryes}
    html_template = loader.get_template("home/app_news.html")
    return HttpResponse(html_template.render(context, request))
