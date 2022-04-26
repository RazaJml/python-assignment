"""
Views for shortify app.
"""
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from shortify.models import ShortenedUrl


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def shortify(request):
    """
    API endpoint to shortify the URL.
    """
    url = request.data.get('url')
    if not url:
        return Response({'error': 'URL is required.'}, status=status.HTTP_400_BAD_REQUEST)
    shortened_url = ShortenedUrl.create(url)

    return Response({
        'shortened_url': request.build_absolute_uri(shortened_url.shortened_url)
    })


@require_http_methods(['GET'])
def url_redirect(request, token):
    """
    Redirect the user to the original URL.
    """
    shortened_url = ShortenedUrl.objects.filter(token=token).first()
    if not shortened_url:
        return Response({'error': 'Invalid URL.'}, status=status.HTTP_404_NOT_FOUND)

    return redirect(shortened_url.url)
