from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('Episode/<int:pk>/',views.EpisodeDetail, name='detail' ),
]
