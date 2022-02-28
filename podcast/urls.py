from django.urls import path
from . import views
# from .views import RatingUpdateView

urlpatterns = [
    path('', views.home, name='home'),
    path('Episodes', views.explore, name='episodes'),
    path('Episode/<int:pk>/', views.EpisodeDetail, name='detail'),
    path('Episode/<int:pk>/rate', views.Rate, name='rate'),
    path('episode/<int:pk>/addtofavs', views.addToFavorites, name="addtofavorites"),
    path('favorites/', views.favorites, name="favorites"),
    path('categories/', views.Categories, name="categories"),
    path('rating/<int:pk>/delete', views.ratingDelete, name="comment-delete"),
    path('rating/<int:pk>/update', views.ratingUpdate, name="comment-update")
    # path('rating/<int:pk>/update', RatingUpdateView.as_view(), name='comment-update'),


]
