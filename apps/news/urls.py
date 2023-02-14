from django.urls import path
from . import views

urlpatterns = [path("", views.app_news, name="app_news")]
