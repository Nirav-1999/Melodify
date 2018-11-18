from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from django.views import generic
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import View

from django.urls import reverse_lazy

from .models import Album,Song
from .serializers import AlbumSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly

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
    fields='__all__'

class AlbumDeleteView(LoginRequiredMixin,generic.DeleteView):
    model=Album
    success_url=reverse_lazy('music:songs')

class SongCreateView(LoginRequiredMixin,generic.CreateView):
    model=Song
    template_name='song_new.html'
    fields='__all__'

class SongDeleteView(LoginRequiredMixin,generic.DeleteView):
    model=Song
    success_url=reverse_lazy('music:songs')



#API-Views

class AlbumViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    

