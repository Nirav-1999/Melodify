from django.conf.urls import url
from . import views

app_name='accounts'

urlpatterns = [
    #accounts/signup/
    url(r'^signup/',views.SignUpView.as_view(),name='signup'),
]