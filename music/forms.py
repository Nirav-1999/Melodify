from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ('album',)
        fields = ['audio_file','song_title']