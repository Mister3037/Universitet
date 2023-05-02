from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def salomlash(sorov):
    return HttpResponse("<h1>Salom, Dunyo!</h1>")

def bosh_sahifa(request):
    return render(request, 'home.html')

def mening_kitoblarim(request):
    content = {
        'kitoblar': ["Ufq", "Qo'rqma", "O'tkan kunlar", "Odamiylik mulki"],
        "ism": "Zafarjon"
    }
    return render(request, 'kitoblar.html', content)

def talabalar(request):
    content = {
        'students':Talaba.objects.all()
    }
    return render(request, 'talabalar.html', content)

def bitiruvchi_talaba(request):
    content = {
        'bitiruvchilar': Talaba.objects.filter(bitiruvchi=True)
    }
    return render(request, 'bitiruvchi.html', content)

def bitta_talaba(request, son):
    content = {
        "talaba":Talaba.objects.get(id=son)
    }
    return render(request, 'bitta_talaba.html', content)

def shahar(request):
    return HttpResponse("<h1>Salom Manchester!</h1>")

def city(request):
    return HttpResponse("<h3>Salom Zafarjon! Brighton shahriga hush kelibsiz!</h3>")

#3

