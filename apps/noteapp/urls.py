from django.urls import path
from .views import app_notes

urlpatterns = [
    # The home page
    path("app_notes.html", app_notes, name="app_notes")
]
