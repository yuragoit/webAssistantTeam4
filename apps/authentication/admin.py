# -*- encoding: utf-8 -*-


from django.contrib import admin

# Register your models here.
from .models import Tag, Note, NoteToTag

# Register your models here.
admin.site.register(Tag)
admin.site.register(Note)
admin.site.register(NoteToTag)
