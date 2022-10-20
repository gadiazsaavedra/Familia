from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render



def saludo(request):

    misaludo = open('I:/Python/Proyectos/Familia/mifamilia/mifamilia/mifamilia/templates/t1.html')

    miplantilla = Template(misaludo.read())

    misaludo.close()

    micontexto = Context()

    documento = miplantilla.render(micontexto)

    return HttpResponse(documento)

