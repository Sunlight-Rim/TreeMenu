from django.shortcuts import render


def index(request):
    return render(request, 'menu/index.html', {
        'title': 'Menu',
        'path': request.path.rstrip('\\')
    })