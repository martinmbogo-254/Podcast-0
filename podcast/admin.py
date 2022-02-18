from django.contrib import admin
from .models import Season, Episode, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Season)
admin.site.register(Episode)