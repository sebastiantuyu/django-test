from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render,redirect
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



def log_out(request):
    """
    Hacer logout de la sesion de usuairo
    """
    logout(request)
    return redirect('login')