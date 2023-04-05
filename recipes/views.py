from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Matheus Ricardo'
    })

def contato(request):
    return render(request, 'temp/temp.html')


def sobre(request):
    return HttpResponse("<h1>Sobre!</h1>")




