from django.urls import path
from . import views
# from .views import app_notes

urlpatterns = [
    # The home page
    path("", views.app_storage, name="app_storage")
]
