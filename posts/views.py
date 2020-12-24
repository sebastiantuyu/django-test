from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
# Create your views here.

informacion = [{
    'name':'Sebastian Tuyu',
    'user':'alextp',
    'timestamp': datetime.now().strftime("%b %d"),
} ,
{
    'name':'Emiliano Tuyu',
    'user':'emitp',
    'timestamp': datetime.now().strftime("%b %d"),
},
{
    'name':'Mau Tuyu',
    'user':'mauricioTP',
    'timestamp': datetime.now().strftime("%b %d"),
}
]



def post(request):
    """ POST EXISTENTES """
    contact = []
    for posts in informacion:
        contact.append("""
            <p>{name}</p>
            <p>{user}</p>
            <p>{timestamp}</p>
        """.format(**posts))

    return HttpResponse('<br>'.join(contact))