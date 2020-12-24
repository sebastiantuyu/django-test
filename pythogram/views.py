""" Seccion de vistas para Django """
from django.http import HttpResponse,JsonResponse

#Utiliadades
from datetime import datetime
import json

def hello_world(rquest):
    """ Vistas de prueba para Django """
    now = datetime.now().strftime('%b %dth, %Y - %H:%H hrs')
    return HttpResponse("Probando las vistas {now}".format(now=str(now)))

def hi(request):
    """ Ejectuar consola ---> import pdb; pdb.set_trace()"""
    numbers = request.GET['numbers'].split(',')
    # numbers = [int(i) for i in request.GET['numbers']]
    numbers = [int(i) for i in numbers]
    sorted_int = sorted(numbers)
    dic = {}
    for i in numbers:
        dic[str(i)] = [i]
    response = JsonResponse(dic, safe=False)
    return HttpResponse("Esto son los numeros {0}".format(response.content))

def FormatoJson(request):
    numbers = request.GET['numbers'].split(',')
    numbers = sorted(numbers)
    data ={
            'status':'ok',
            'numbers': numbers,
            'message': 'Integers succesfully ordered'
        }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def Argumentos(request,name,age):
    if age < 12:
        return HttpResponse("Im sorry {0} you're not allowed here :( ".format(name))
    else:
        return HttpResponse("Tu usuario es {0} y tienes {1} años".format(name,age))