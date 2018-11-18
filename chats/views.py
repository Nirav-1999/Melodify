from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import CreateView
from django.http import request,HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from .models import Chats
from .forms import ChatForm

class ChatView(LoginRequiredMixin,generic.ListView):
    model=Chats
    template_name='chats.html'
    context_object_name='chats'
    login_url='login'

    def get_queryset(self):
        return Chats.objects.all()
    
    
    def post(self,request):
        new_flow={}
        if request.user.is_authenticated:
            if request.method=='POST':
                form=ChatForm(request.POST)
                if form.is_valid():
                    new_flow=form.save(commit=False)
                    name=request.user
                    new_flow.user=name
                    new_flow.save()
        return redirect(reverse('chats:chats-index'))


    