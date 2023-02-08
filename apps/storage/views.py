from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def app_storage(request):
    context = {"text": "Render test passed. Team, please add you view content from developed APP to appropriate html file inside class page-wrapper"}

    html_template = loader.get_template("home/app_file_storage.html")
    return HttpResponse(html_template.render(context, request))
