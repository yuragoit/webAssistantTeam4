from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def app_notes(request):
    context = {"text": "Helo world"}

    html_template = loader.get_template("home/app_notes.html")
    return HttpResponse(html_template.render(context, request))
