from django.db import models

# Create your models here.
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=20, null= True)
    bio = models.TextField(max_length=1000, null= True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    image = models.FileField( upload_to='uploads',blank=True)
    name = models.TextField(max_length=500,null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100 , default='project', null= True)
    description = models.TextField(max_length=250, null= True)
    technology = models.TextField(max_length=50, null= True)
    status = models.CharField(max_length=20 ,default='done', null= True)
    source = models.TextField(default='link', null= True)


    def __str__(self):
        return self.name
