import os
from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import File
from .сonstans import REGISTER_EXTENSIONS, UPLOADS_DIR


# Create your views here.
def get_folder_name(filename):
    extension = Path(filename).suffix[1:].upper()
    for key, list_value in REGISTER_EXTENSIONS.items():
        if extension in list_value:
            return key
    else:
        return 'Others'


@login_required(login_url="/login/")
def upload(request):
    if request.method == 'POST' and request.FILES['upload_file']:
        file = request.FILES['upload_file']
        filename = file.name
        if os.path.exists(Path(f'{UPLOADS_DIR}/{get_folder_name(filename)}/{filename}')):
            os.remove(Path(f'{UPLOADS_DIR}/{get_folder_name(filename)}/{filename}'))
        fs = FileSystemStorage(location=Path(f'{UPLOADS_DIR}/{get_folder_name(filename)}'))
        fs.save(name=filename, content=file)
        # model_file = File(file=file, name=filename, type=get_folder_name(filename), owner=request.user)
        # model_file.save()
        return redirect('home/app_file_storage.html')
    return render(request, 'home/app_file_storage.html')
