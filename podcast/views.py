from django.shortcuts import render
from .models import Category, Episode

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''
    episodes = Episode.objects.filter(title__icontains=q)
    categories= Category.objects.all()
    episodes = Episode.objects.all()
    context={
        'categories': categories,
        'episodes': episodes,
    }
    return render(request, 'podcast/home.html', context)



def EpisodeDetail(request, pk):
    episode = Episode.objects.get(id=pk)
    # ratings = Rating.objects.filter(post=post)
    # average_ratings = ratings.aggregate(Avg('rate'))
    # total_ratings = ratings.count()
    context = {
        'episode': episode,
        # 'average_ratings': average_ratings,
        # 'ratings': ratings,
        # 'total_ratings': total_ratings,
    }
    return render(request, 'podcast/episode.html', context)