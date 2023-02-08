from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import Tag, Note


# Create your views here.
def app_notes(request):
    context = {"text": "Render test passed"}

    html_template = loader.get_template("home/app_notes.html")
    return HttpResponse(html_template.render(context, request))
