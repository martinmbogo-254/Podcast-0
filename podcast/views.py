from multiprocessing import context

from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Avg
from .models import Category, Episode, Rating
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from .forms import RateForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

def home(request):
    recent_episodes = Episode.objects.filter().order_by('-posted')[:3]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'recent_episodes': recent_episodes
    }
    return render(request, 'podcast/home.html', context)


def explore(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    episodes = Episode.objects.filter(
        Q(title__icontains=q) |
        Q(category__name__icontains=q) |
        Q(desc__icontains=q)
    )
    no_episodes = episodes.count()

    categories = Category.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(episodes, 4)
    try:
        episodes = paginator.page(page)
    except PageNotAnInteger:
        episodes = paginator.page(1)
    except EmptyPage:                                                       
        episodes = paginator.page(paginator.num_pages)

    context = {
        'episodes': episodes,
        'categories' :categories,
        'no_episodes':no_episodes

    }
    return render(request, 'podcast/Explore.html', context)




def EpisodeDetail(request, pk):
    episode = Episode.objects.get(id=pk)
    ratings = Rating.objects.filter(episode=episode)
    average_ratings = ratings.aggregate(Avg('rate'))
    fav = bool
    if episode.favorite.filter(id=request.user.id).exists():
        fav = True
    total_ratings = ratings.count()
    context = {
        'episode': episode,
        'average_ratings': average_ratings,
        'ratings': ratings,
        'total_ratings': total_ratings,
        'fav': fav,
    }
    return render(request, 'podcast/episode.html', context)


@login_required(login_url='login')
def Rate(request, pk):
    # getting post objects by their id
    episode = Episode.objects.get(id=pk)
    user = request.user

    # form method
    if request.method == 'POST':
        form = RateForm(request.POST)
        # validating the form.
        if form.is_valid():
            rate = form.save()
            rate.episode = episode
            rate.user = user
            rate.save()
            return HttpResponseRedirect(reverse('detail', args=[pk]))
    else:
        form = RateForm()
    context = {
        'form': form,
        'episode': episode,

    }
    return render(request, 'podcast/rate.html', context)


@login_required(login_url='login')
def favorites(request):
    user = request.user
    favorites = Episode.objects.filter(favorite=user)
    fav_episodes = Episode.objects.filter(favorite=user).count()
    context = {
        'favorites': favorites,
        'fav_episodes': fav_episodes
    }
    return render(request, 'podcast/favorites.html', context)


@login_required(login_url='login')
def addToFavorites(request, pk):
    episode = Episode.objects.get(id=pk)
    if episode.favorite.filter(id=request.user.id).exists():
        episode.favorite.remove(request.user)
    else:
        episode.favorite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def ratingDelete(request, pk):
    rating = Rating.objects.get(id=pk)
    if request.method == 'POST':
        rating.delete()
        return redirect('home')
    context = {
        'rating': rating,
    }
    return render(request, 'podcast/delete.html', context)


def ratingUpdate(request, pk):
    rating = Rating.objects.get(id=pk)
    form = RateForm(instance=rating)
    if request.method == "POST":
        form = RateForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            comment = form.cleaned_data.get('comment')
            messages.success(request, f'comment successfully updated !!')
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'podcast/rateupdate.html', context)
