from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.utils import IntegrityError
from django.views.generic import DetailView
from .models import Profile
from .forms import ProfileForm, SignupForm
from posts.models import Post
# Create your views here.

class UserDetailView(DetailView):

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'


    def get_context_data(self, **kwargs):
        """ Agregar los datos de contexto (extras) del usuario """

        context = super().get_context_data(**kwargs)
        user= self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

def user_view(request):
    """

        Vista para iniciar sesion recibiendo dos parametros que el usuario acaba de enviar como POST

    """
    if request.method == 'POST':
        print('*'*5)
        user_name = request.POST['username']
        passw = request.POST['password']
        user = authenticate(request,username=user_name,password=passw)
        if user is not None:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render(request, "users/login.html",{'error':'Usuario o contraseña invalidos'})
    return render(request, "users/login.html")


@login_required
def log_out(request):
    """
    Hacer logout de la sesion de usuairo
    """
    logout(request)
    return redirect('users:login')

def sign_up(request):
    """ AGREGAR SIGN UP PARA USUARIOS """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    return render(request, 'users/sign_up.html', {'form':form})




def update_profile(request):
    """
        Actualizar perfil, utilizando un MIDDLEWARE
    """
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.bio = data['bio']
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()

            # Necesitamos escribir correctamente la URL usando reverse
            url = reverse('users:detail',kwargs={'username':request.user.username})
            return redirect(url)
    else:
        form = ProfileForm() 
    
    return render(request,'users/update_profile.html',context={'profile':profile,'form':form})





