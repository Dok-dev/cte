from django.shortcuts import render
from django.views import generic
from projects.models import (
    Project,
    # PrivateCloudPassport,
    # S3Passport,
    # MinimalYaml,
    # ProjectDocuments,
    # Manufacturer,
    # Equipment,
    # Server,
    # Switch,
    # Storage
)

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_progects=Project.objects.all().count()
    # Доступные книги (статус = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    # num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_progects':num_progects},
    )
