from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import CustomUser

from django.contrib import admin


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role', 'created_at')
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {'fields': (
            'username', 'first_name', 'last_name', 'email', 'password', 'is_superuser', 'is_staff', 'is_active',
            'role', 'phone_number', 'address', 'city', 'state', 'country', 'image')}),)
    add_fieldsets = (
        (None, {
            'fields': (
                'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active',
                'is_superuser', 'role', 'phone_number', 'address', 'city', 'state', 'country', 'image'), }),)
    search_fields = ('username', 'email')
    ordering = ('-id', 'username')
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
