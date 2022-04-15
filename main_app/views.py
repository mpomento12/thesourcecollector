from http.client import TOO_MANY_REQUESTS
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Album, Format
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
    id_list = album.formats.all().values_list('id')
    formats_album_doesnt_have = Format.objects.exclude(id__in=id_list)
    listening_form = ListeningForm()
    return render(request, 'albums/detail.html', {
        'album': album, 
        'listening_form': listening_form, 
        'formats': formats_album_doesnt_have
    })

def assoc_format(request, album_id, format_id):
    Album.objects.get(id=album_id).formats.add(format_id)
    return redirect('detail', album_id=album_id)

class AlbumCreate(CreateView):
    model = Album
    fields = ['title', 'artist', 'label', 'release']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['label', 'release']

class AlbumDelete(DeleteView):
    model = Album
    success_url = '/albums/'

def add_listening(request, album_id):
  form = ListeningForm(request.POST)
  if form.is_valid():
      new_listening = form.save(commit=False)
      new_listening.album_id = album_id
      new_listening.save()
  return redirect('detail', album_id=album_id)

class FormatList(ListView):
    model = Format

class FormatDetail(DetailView):
    model = Format

class FormatCreate(CreateView):
    model = Format
    fields = '__all__'

class FormatUpdate(UpdateView):
    model = Format
    fields = ['name']

class FormatDelete(DeleteView):
    model = Format
    success_url = '/formats/'
