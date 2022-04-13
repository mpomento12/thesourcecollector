from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Listening
from .forms import ListeningForm

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
    listening_form = ListeningForm()
    return render(request, 'albums/detail.html', {'album': album, 'listening_form': listening_form})

def add_listening(request, album_id):
  form = ListeningForm(request.POST)
  if form.is_valid():
      new_listening = form.save(commit=False)
      new_listening.album_id = album_id
      new_listening.save()
  return redirect('detail', album_id=album_id)
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

