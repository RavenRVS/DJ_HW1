import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time.strftime("%H:%M:%S")}'
    return HttpResponse(msg)


def workdir_view(request):
    list_dir = os.listdir()
    msg = f'В директоории проекта следующие файлы: {list_dir}'
    return HttpResponse(msg)
