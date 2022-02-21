from django.contrib import admin
from .models import Season, Episode, Category,Rating

# Register your models here.
admin.site.register(Category)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Rating)

admin.site.site_header = "SHE-HUDRAY ADMIN"
admin.site.site_title = "SHE-HUDRAY ADMIN AREA"