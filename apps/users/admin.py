from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff", "is_active", "is_superuser")
    list_display_links = ("id", "username")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active", "is_superuser")
    list_editable = ("is_staff", "is_active", "is_superuser")


admin.site.register(User, UserAdmin)
