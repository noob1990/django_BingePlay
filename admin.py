from django.contrib import admin
from .models import Watchlist

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'added_at')  # Display user, title, and date added
    search_fields = ('user__username', 'title')  # Enable searching by user and movie title
    list_filter = ('user',)  # Filter watchlist entries by user

admin.site.register(Watchlist, WatchlistAdmin)


