from django.urls import path
from django.views.generic import TemplateView

from posts import views
from .views import post, create_post, PostFeed

urlpatterns = [
    # FEED
    path('', PostFeed.as_view(), name='feed'),
    # CREATE NEW POST
    path('newpost/', create_post, name="create"),

]