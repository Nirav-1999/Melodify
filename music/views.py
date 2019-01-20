from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import viewsets

from django.shortcuts import get_object_or_404, render, redirect

from django.views import generic
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import View
from django.core import serializers
from django.urls import reverse_lazy
from django.http import request, HttpRequest

from .models import Album,Song
from .serializers import AlbumSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly
from .forms import SongForm

from importlib import import_module
from django.conf import settings

import requests

User=get_user_model()


# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class SongsView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'songs.html'
    
class AllAlbumsView(LoginRequiredMixin,generic.ListView):
    model=Album
    template_name='all_albums.html'
    context_object_name='albums'
    login_url='login'
    def get_queryset(self):
        return Album.objects.all()

    
class AlbumDetailView(LoginRequiredMixin,generic.DetailView):
    model = Album
    template_name = "detail.html"
    login_url='login'
   




    
class AlbumCreateView(LoginRequiredMixin,generic.CreateView):
    model=Album
    template_name='album_new.html'
    fields=['album_title','artist','genre','album_logo']
    login_url='login'
    def form_valid(self,form):
        form.instance.owner=self.request.user
        form.save()
        return redirect(reverse('music:all-albums'))


class AlbumDeleteView(LoginRequiredMixin,generic.DeleteView):
    model=Album
    success_url=reverse_lazy('music:all-albums')
    login_url='login'

class SongCreateView(LoginRequiredMixin,generic.CreateView):
    model=Song
    template_name='song_new.html'
    form_class = SongForm
    login_url='login'

    def post(self,request):
        new_flow={}
        if 'album_title' in request.POST:
            album_title = request.POST['album_title']
            album = Album.objects.filter(album_title__startswith = album_title)
            self.request.session['album'] = serializers.serialize('json',album)
            print(self.request.session['album'])
            return redirect(reverse('music:add-song'))
        elif request.method == 'POST':
            form = SongForm(request.POST)
            print(form)
            if form.is_valid():
                new_flow=form.save(commit=False)
                new_flow.album=self.request.session['album']
                print(new_flow)
                print(44)
                new_flow.save()
            else:
                print("Invalid form")
                print(form.errors)
              
               
            return redirect(reverse('music:all-albums'))
            



        



   
class SongDeleteView(LoginRequiredMixin,generic.DeleteView):
    model=Song
    success_url=reverse_lazy('music:all-albums' )
    login_url='login'


#REST-API-Views

class AlbumViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    

#LAST.FM-API-VIEWS
def lastfmApiGetAlbum(request):
    album={}
    songs=[]
    album_img_url=''
    if 'album' in request.GET:
   
        album_name=request.GET['album']
        artist=request.GET['artist']
        api_key='4b6e8d87aa5c790a95ca2bfc693fd9f4'
        api_url='http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={key}&artist={artist}&album={album}&format=json'.format(key=api_key,artist=artist,album=album_name)
        album_get_url=requests.get(api_url)
        search_was_successful = (album_get_url.status_code == 200)  # 200 = SUCCESS
        album=album_get_url.json()
        album['success'] = search_was_successful
        a=album['album']
        b=a['image']
        album_img_url=b[3]['#text']
        c=a['tracks']
        d=c['track']
        for tracks in d:
            songs.append([tracks['name'],tracks['duration']])
            
       
    return render(request,'last_fm.html',{
        'album':album,
        'img_url':album_img_url,
        'songs':songs,
        }
        )
