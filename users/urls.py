from django.urls import path
from django.views.generic import TemplateView
from users import views
from .views import LogOutView,\
                   sign_up,\
                   LoginViewClass,\
                   UserDetailView,\
                   SignupFormView,\
                   UpdateProfileView



urlpatterns = [


    # MANAGEMENT DE USUARIOS

    path('logout/', LogOutView.as_view(), name='logout'),

    # VISTA BASADA EN CLASES PARA HACER LOGIN
    path('login/', LoginViewClass.as_view(), name='login'),

    # VISTA BASADA EN CLASES PARA HACER UPDATE

    path('me/profile', UpdateProfileView.as_view(), name='update'),

    # VISTA BASADA EN CLASE SIGN UP
    path('signup/', SignupFormView.as_view(), name='sign_up'),

    # VISTA BASADA EN CLASE DEL PERFIL DE USUARIO
    path(
        route='<str:username>/',
        view= UserDetailView.as_view(),
        name='detail'
    ),
]
