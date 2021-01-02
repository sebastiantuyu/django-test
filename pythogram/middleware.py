"""  Aqui van todos los comandos del MiddleWare """
from django.shortcuts import redirect,reverse

class ProfileCompletionMiddleware:
    """
        Comprobar que un usuario tenga su foto de perfil y biografia
        escrita, si no, no puede navegar
    """


    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
            Codigo que va a ser ejecutado antes de imprimir la vista
        """

        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.bio:
                    if request.path not in [reverse('update'),reverse('logout')]:
                        return redirect('update')

        response = self.get_response(request)
        return response
