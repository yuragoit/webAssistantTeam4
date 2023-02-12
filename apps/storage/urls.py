from django.urls import path
from . import views

app_name = 'storage'

urlpatterns = [
    # The home page
    path("", views.upload, name="upload"),
    path("archives/", views.archives, name="archives"),
    path("images/", views.images, name="images"),
    path("video/", views.video, name="video"),
    path("documents/", views.documents, name="documents"),
    path("programs/", views.programs, name="programs"),
    path("audio/", views.audio, name="audio"),
    path("others/", views.others, name="others"),
]
