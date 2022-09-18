from django.shortcuts import render


def redoc(request):
    return render(request, 'templates/Redoc.html')


def redoc_json(request):
    return render(request, 'templates/redoc-2.json')
