from django.contrib import admin
from .models import Links, UserFiles, UserDirs


class NewLinks(admin.ModelAdmin):
    list_display = ('id', 'link', 'description', 'created_at', 'is_published', 'tags')
    list_display_links = ('id', 'link')
    search_fields = ('tags', 'description')


admin.site.register(Links, NewLinks)
admin.site.register(UserFiles)
admin.site.register(UserDirs)
