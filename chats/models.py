from django.db import models
from django.urls import reverse


class Chats(models.Model):
    user=models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    chat=models.TextField()
    
    def get_absolute_url(self):
        return reverse('chats:chats-index')

    def __str__(self):
        return self.chat
        
