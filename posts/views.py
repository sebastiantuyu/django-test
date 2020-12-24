from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

informacion = [
    {
        'title': 'Mi primer post in Pytagram',
        'user': {
            'name': 'alextpineiro',
            'ppic': 'https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-512.png',
        },
        'timestamp': datetime.now().strftime("%b %d"),
        'postImage': 'https://librosostenibilidad.files.wordpress.com/2017/03/paisaje-cultura-sostenibilidad-2.jpg',
    },

    {
        'title': 'Este es el tercer post',
        'user': {
            'name': 'emituyupp',
            'ppic': 'https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-512.png',
        },
        'timestamp': datetime.now().strftime("%b %d"),
        'postImage': 'https://librosostenibilidad.files.wordpress.com/2017/03/paisaje-cultura-sostenibilidad-2.jpg',
    },

    {
        'title': 'jugando con Pytagram',
        'user': {
            'name': 'mauricioBlodBoster',
            'ppic': 'https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-512.png',
        },
        'timestamp': datetime.now().strftime("%b %d"),
        'postImage': 'https://librosostenibilidad.files.wordpress.com/2017/03/paisaje-cultura-sostenibilidad-2.jpg',
    },


]


def post(request):
    """ POST EXISTENTES """
    return render(request, 'feed.html', {'info': informacion})
