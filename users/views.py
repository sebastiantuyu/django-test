from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from .models import Profile
from .forms import ProfileForm, SignupForm

# Create your views here.




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
            return redirect('feed')
        else:
            return render(request, "users/login.html",{'error':'Usuario o contraseña invalidos'})
    return render(request, "users/login.html")


@login_required
def log_out(request):
    """
    Hacer logout de la sesion de usuairo
    """
    logout(request)
    return redirect('login')

def sign_up(request):
    """ AGREGAR SIGN UP PARA USUARIOS """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
            print('*'*20)
            print("ok")
            print('*'*20)
            return redirect('update')
    else:
        form = ProfileForm() 
    
    return render(request,'users/update_profile.html',context={'profile':profile,'form':form})





