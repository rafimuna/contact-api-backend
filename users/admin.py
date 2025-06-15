from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Admin table list view
    list_display = (
        "username", "email", "first_name", "last_name", "phone", "gender", "is_staff"
    )

    # Fieldsets for user detail view in admin (edit form)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("phone", "gender")}),
    )

    # Fieldsets for user creation form in admin (add form)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("phone", "gender")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
