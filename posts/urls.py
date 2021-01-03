from django.urls import path
from django.views.generic import TemplateView

from posts import views
from .views import post, create_post

urlpatterns = [
    # FEED
    path('', post, name='feed'),
    # CREATE NEW POST
    path('newpost/', create_post, name="create"),

]