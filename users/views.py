from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
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

    if request.method == "POST":
        username = request.POST['username']
        passw = request.POST['password']
        passw_conf = request.POST['password-confirmation']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if passw != passw_conf:
            return render(request, 'users/sign_up.html',{'info':'Las contraseñas deben ser iguales'})
    return render(request, 'users/sign_up.html')