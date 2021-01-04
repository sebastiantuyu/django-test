from django.urls import path
from django.views.generic import TemplateView

from posts import views
from .views import post, create_post, PostFeed, PostDetails

urlpatterns = [
    # FEED
    path('', PostFeed.as_view(), name='feed'),

    # DETAIL POST
    path('<int:pk>/',PostDetails.as_view(),name="detail"),

    # CREATE NEW POST
    path('newpost/', create_post, name="create"),

]