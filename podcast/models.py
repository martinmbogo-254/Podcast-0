from django.db import models

# Create your models here.

class Season(models.Model):
    title= models.CharField(max_length=100)


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
    season =models.ForeignKey(Season, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    thumbnail = models.FileField(upload_to='episodes/', default='episodes/default.png')
    posted = models.DateTimeField( auto_now_add=True,null=True)
    # audio
     
    def __str__(self):
        return self.title

    def desc_snippet(self):
        return self.desc[:60]
