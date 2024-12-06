from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    tmdb_id = models.IntegerField()  # Store TMDb movie ID
    title = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    overview = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
