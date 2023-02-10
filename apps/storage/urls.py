from django.urls import path
from . import views
# from .views import app_notes

app_name = 'storage'

urlpatterns = [
    # The home page
    path("", views.upload, name="upload")
]
