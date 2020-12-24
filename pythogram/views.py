""" Seccion de vistas para Django """
from django.http import HttpResponse

def hello_world(rquest):
    """ Vistas de prueba para Django """
    return HttpResponse("Probando las vistas")
