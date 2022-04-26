"""
Serializers for API authentication.
"""
from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user model.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', )


class RegisterSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        raise serializers.ValidationError('method not supported.')

    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Validate that user with given username and email does not already exist.
        """
        username = data['username']
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(f'User with username "{username}" already exists.')

        email = data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(f'User with email "{email}" already exists.')

        return data

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
