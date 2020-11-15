from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')
    #return HttpResponse('Hello, Home page works!')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!#+*><-_/(){}[]%&$§€'))

    length = int(request.GET.get('length'))

    generated_Password = ''

    for i in range(length):
        generated_Password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':generated_Password})

def about(request):
    return  render(request, 'about/about.html')