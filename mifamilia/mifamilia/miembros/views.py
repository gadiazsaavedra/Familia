from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Miembro

def cargarmiembro(request, nombre, fecha_nac, edad):

    miembro = Miembro(nombre=nombre, fecha_nac=fecha_nac, edad=edad)
    miembro.save()
    mensaje = f'El miembro {nombre} se cargo correctamente'

    return HttpResponse(mensaje) 
