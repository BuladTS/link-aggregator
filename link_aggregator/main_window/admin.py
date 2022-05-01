from django.contrib import admin
from .models import User_data, Users, Links


class NewLinks(admin.ModelAdmin):
    list_display = ('id', 'link', 'description', 'created_at', 'is_published', 'tags')
    list_display_links = ('id', 'link')
    search_fields = ('tags', 'description')


admin.site.register(User_data)
admin.site.register(Links, NewLinks)
