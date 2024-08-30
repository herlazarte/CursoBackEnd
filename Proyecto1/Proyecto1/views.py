from django.http import HttpResponse
from django.shortcuts import render

def saludo(request): ##primera vista

    return render(request, "miplantilla.html",{})

def despedida(request):
    return HttpResponse("chau")