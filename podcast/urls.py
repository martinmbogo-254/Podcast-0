from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('Episodes',views.explore, name='episodes' ),
    path('Episode/<int:pk>/',views.EpisodeDetail, name='detail' ),
    
]
