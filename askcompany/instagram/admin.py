from django.contrib import admin

from askcompany.instagram.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
