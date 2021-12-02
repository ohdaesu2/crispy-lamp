from django.contrib import admin

from askcompany.instagram.models import Post


@admin.register()
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'message', 'is_public']
    list_display_links = ['message']