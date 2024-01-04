from django.contrib import admin
from .models import Post, Like


class PostAdmin(admin.ModelAdmin):
    ordering = ['-updated_at']
    list_display = ['title', 'created_at']
    list_filter = ['user']
    search_fields = ['text']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Like)
