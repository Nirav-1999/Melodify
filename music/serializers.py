from .models import Album,Song
from rest_framework import serializers
from accounts.models import CustomUser


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model=Album
        fields=('id','owner','album_title','artist','genre','album_logo')
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    albums=serializers.HyperlinkedRelatedField(many=True, view_name='music:album-detail',read_only=True)    

    class Meta:
        model=CustomUser
        fields=('id','username','albums')