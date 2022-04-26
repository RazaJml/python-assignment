"""
admin views for shortify app.
"""
from django.contrib import admin

from shortify.models import ShortenedUrl


@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):
    """
    Model admin for shortened url.
    """
    list_display = ('id', 'url', 'token', 'created_at', 'updated_at', )
    search_fields = ('id', 'url', 'token', )
