from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
## TODO:
def home(request):
    return render(request, 'generator/home.html', {'password':'dfsfsdfsdfsscw'})

def about_me(request):
    return render(request, 'generator/about_me.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length') or 12)

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    thepassword = ''
    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword})
