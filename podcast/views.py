from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Avg
from .models import Category, Episode, Rating
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from .forms import RateForm


# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''
    episodes = Episode.objects.filter(title__icontains=q)
    categories= Category.objects.all()
    # episodes = Episode.objects.all()
    context={
        'categories': categories,
        'episodes': episodes,
    }
    return render(request, 'podcast/home.html', context)

def explore(request):
    episodes = Episode.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(episodes, 4)
    try:
        episodes = paginator.page(page)
    except PageNotAnInteger:
        episodes= paginator.page(1)
    except EmptyPage:
        episodes = paginator.page(paginator.num_pages)



    context={
        'episodes': episodes,
        
    }
    return render(request,'podcast/explore.html',context)

def EpisodeDetail(request, pk):
    episode = Episode.objects.get(id=pk)
    ratings = Rating.objects.filter(episode=episode)
    average_ratings = ratings.aggregate(Avg('rate'))
    total_ratings = ratings.count()
    context = {
        'episode': episode,
        'average_ratings': average_ratings,
        'ratings': ratings,
        'total_ratings': total_ratings,
    }
    return render(request, 'podcast/episode.html', context)


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