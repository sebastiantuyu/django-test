""" Seccion de vistas para Django """
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Utiliadades
from datetime import datetime
import json


def FormatoJson(request):
    numbers = request.GET['numbers'].split(',')
    numbers = sorted(numbers)
    data ={
            'status':'ok',
            'numbers': numbers,
            'message': 'Integers succesfully ordered'
        }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


