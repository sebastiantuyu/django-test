"""pythogram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import FormatoJson
from posts.views import post,create_post
from users.views import user_view,log_out,sign_up,update_profile

urlpatterns = [
    path('format-j-2/',FormatoJson),
    path('',post,name='feed'),
    path('admin/', admin.site.urls),
    path('login/',user_view, name='login'),
    path('logout/',log_out,name='logout'),
    path('signup/',sign_up,name='sign_up'),
    path('newpost/',create_post,name="new_post"),
    path('users/me/profile',update_profile,name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

