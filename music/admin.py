from django.contrib import admin
from .models import Album,Song
# Register your models here.

class SongInline(admin.TabularInline):
    model=Song
    extra=1

class AlbumAdmin(admin.ModelAdmin):
    fieldsets=[('Album_Info',{'fields':['owner','album_title','artist','genre','album_logo']})]
    inlines=[SongInline]

admin.site.register(Album,AlbumAdmin)

