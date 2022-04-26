"""
Models for shortify app.
"""
import secrets

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def get_token():
    """
    Get a unique token.
    """
    return secrets.token_urlsafe(5)


class ShortenedUrl(models.Model):
    """
    Model for storing shortened and original URLs.
    """
    url = models.URLField(help_text=_('Original URL to shorten.'))
    token = models.SlugField(help_text=_('Shorthand slug for the above URL.'), default=get_token, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Shortened URL'
        verbose_name_plural = 'Shortened URLs'

    def __str__(self):
        """
        Human-readable representation.
        """
        return f'<ShortenedUrl url="{self.url}">'

    def __repr__(self):
        """
        Uniquely identifying representation.
        """
        return f'<ShortenedUrl id="{self.id}" url="{self.url}">'

    @classmethod
    def create(cls, url):
        """
        Helper method to create a shortened URL.
        """
        instance, _ = cls.objects.get_or_create(url=url)
        return instance

    @property
    def shortened_url(self):
        """
        Return the shortened url.
        """
        return reverse('shortify:redirect', args=(self.token, ))
