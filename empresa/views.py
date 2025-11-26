# empresa/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Empresa!")

def cupom(request):
    return HttpResponse("Cupom funcionando!")
