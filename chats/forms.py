from django import forms
from .models import Chats

 
class ChatForm(forms.ModelForm):
    class Meta:
        model=Chats
        exclude=('user',)
        fields=['chat']