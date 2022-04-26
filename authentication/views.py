"""
Views for API authentication.
"""
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from authentication.permissions import IsSelfOrAdmin
from authentication.serializers import RegisterSerializer, UserSerializer
from utils import is_admin


@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token, created = Token.objects.get_or_create(user=user)

    return Response({
        'user': UserSerializer(user, context={'request': request}).data,
        'token': token.key
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    This model view set can be used by admin to perform CRUD on all users while non-admin
    users can perform CRUD on themselves only.
    """
    serializer_class = UserSerializer
    permission_classes = (IsSelfOrAdmin, IsAuthenticated, )

    def get_queryset(self):
        """
        Get queryset based on user's access level.
        """
        if is_admin(self.request.user):
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)
