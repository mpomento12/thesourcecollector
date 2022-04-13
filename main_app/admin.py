from django.contrib import admin

# Register your models here.
from .models import Album, Listening

admin.site.register(Album)

admin.site.register(Listening)