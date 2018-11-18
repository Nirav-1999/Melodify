from django.conf.urls import url
from . import views

app_name='chats'

urlpatterns = [
    url(r'^$',views.ChatView.as_view(),name='chats-index'),
]