from django.urls import path
from .views import NotesListView, NotesDeleteView, note

app_name = "notes"

urlpatterns = [
    path("", NotesListView.as_view(), name="notes_list"),
    path("create/", note, name="note_create"),
    path("detail/<int:pk>/", NotesListView.as_view(), name="note_detail"),
    path("update/<int:pk>/", NotesListView.as_view(), name="note_update"),
    path("delete/<int:pk>/", NotesDeleteView.as_view(), name="note_delete"),
]
