from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.

class PostFeed(LoginRequiredMixin, ListView):
    """
        Clase para imprimir todos los post existentes usando ListView
    """
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'info'

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