from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta: # type: ignore
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        # Create the user with hashed password using `create_user`
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user



from .models import Watchlist

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta: # type: ignore
        model = Watchlist
        fields = ['id', 'tmdb_id', 'title', 'poster_path', 'overview', 'added_at']
