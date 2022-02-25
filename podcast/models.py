from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Season(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.FileField(upload_to='pics/', default='pics/default.png')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    thumbnail = models.FileField(upload_to='episodes/', default='episodes/default.png')
    favorite = models.ManyToManyField(User, blank=True, related_name='favorite')
    audio = models.FileField(upload_to='audio/', default='audio/default.mp3')
    posted = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('episode', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def desc_snippet(self):
        return self.desc[:60]

    def title_snippet(self):
        return self.title[:15]

    class Meta:
        ordering = ['-posted']


RATE_CHOICES = [
    (1, '1-Very Dissatisfied'),
    (2, '2-Dissatisfied'),
    (3, '3-Fair'),
    (4, '4-Satisfied'),
    (5, '5-Very Satisfied'),
]


class Rating(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True,
                                related_name='rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, max_length=50, null=True)
    comment = models.CharField(max_length=100, null=True)
    posted = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('rating', kwargs={'pk': self.pk})
