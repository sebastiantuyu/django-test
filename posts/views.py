from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import PostForm
from .models import Post
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


@login_required
def post(request):
    """ POST EXISTENTES """
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'info':posts})


@login_required
def create_post(request):
    """
        CREACION DE UN NUEVO POST USANDO EL MODEL FORM
    """
    post = Post()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("ok")
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(request,'posts/new_post.html',{'form':form, 'user':request.user})