from django.conf.urls import url
from django.urls import include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from . import views

app_name='music'

schema_view=get_swagger_view(title='Albums API')

router=DefaultRouter()
router.register(r'albums',views.AlbumViewSet)
router.register(r'users',views.UserViewSet)

urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(),name='home'),
    #/music/songs/
    url(r'^songs/$',views.SongsView.as_view(),name='songs'),
    #/music/songs/all-albums/
    url(r'^songs/all_albums/$',views.AllAlbumsView.as_view(),name='all-albums'),
    #/music/songs/1/
    url(r'^songs/(?P<pk>[0-9]+)/$',views.AlbumDetailView.as_view(),name='detail'),
    #/music/album/add
    url(r'^album/add/$',views.AlbumCreateView.as_view(),name='add'),
    #/music/album/2/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDeleteView.as_view(),name='delete'),
    #/music/new_song/
    url(r'^songs/new_song/$',views.SongCreateView.as_view(),name='add-song'),
    #/music/song/2/delete/
    url(r'^song/(?P<pk>[0-9]+)/delete/$',views.SongDeleteView.as_view(),name='song-delete'),
    
    
    #api_views
    url(r'^api/',include(router.urls)),


    #shema-view
    url(r'^schema/$',schema_view),
]

