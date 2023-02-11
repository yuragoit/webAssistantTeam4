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
    if request.method == 'POST' and request.FILES.get('upload_file'):
        file = request.FILES['upload_file']

        filename = file.name
        if os.path.exists(Path(f'{UPLOADS_DIR}/{get_folder_name(filename)}/{filename}')):
            os.remove(Path(f'{UPLOADS_DIR}/{get_folder_name(filename)}/{filename}'))

        fs = FileSystemStorage(location=Path(f'{UPLOADS_DIR}/{get_folder_name(filename)}'))
        fs.save(name=filename, content=file)

        if not File.objects.filter(name=filename, owner=request.user).first():
            model_file = File(name=filename, type=get_folder_name(filename), owner=request.user, size=file.size)
            model_file.save()

        return redirect('home/app_file_storage.html')
    return render(request, 'home/app_file_storage.html')


def render_storage_pages(request, file_type):
    files = File.objects.filter(type=file_type, owner=request.user).all()
    title = file_type
    return render(request, 'storage/files.html', context={'files': files,
                                                          'title': title})


@login_required(login_url="/login/")
def archives(request):
    return render_storage_pages(request, 'Archives')


@login_required(login_url="/login/")
def images(request):
    return render_storage_pages(request, 'Images')


@login_required(login_url="/login/")
def video(request):
    return render_storage_pages(request, 'Video')


@login_required(login_url="/login/")
def documents(request):
    return render_storage_pages(request, 'Documents')


@login_required(login_url="/login/")
def programs(request):
    return render_storage_pages(request, 'Programs')


@login_required(login_url="/login/")
def audio(request):
    return render_storage_pages(request, 'Audio')


@login_required(login_url="/login/")
def others(request):
    return render_storage_pages(request, 'Others')
