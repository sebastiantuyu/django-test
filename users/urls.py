from django.urls import path
from django.views.generic import TemplateView
from users import views
from .views import user_view,log_out,sign_up,update_profile,UserDetailView



urlpatterns = [


    # MANAGEMENT DE USUARIOS
    path('login/', user_view, name='login'),
    path('logout/', log_out, name='logout'),
    path('signup/', sign_up, name='sign_up'),
    path('me/profile', update_profile, name='update'),

    # VISTA BASADA EN CLASE DEL PERFIL DE USUARIO
    path(
        route='<str:username>/',
        view= UserDetailView.as_view(),
        name="detail"
    ),
]
