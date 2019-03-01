from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from music import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('music.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^chats/',include('chats.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^o/',include('oauth2_provider.urls',namespace='oauth2_provider')),
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
