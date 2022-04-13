from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Album

    # Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def albums_index(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})

def albums_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'albums/detail.html', {'album': album})

class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'
    success_url = '/albums/'

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['label', 'release']

class AlbumDelete(DeleteView):
    model = Album
    success_url = '/albums/'
