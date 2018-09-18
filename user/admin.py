from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    # list_display = ()
    # list_filter = ()
    # fieldsets = ()
    readonly_fields = ('created_at', 'date_joined', 'last_login')
    # search_fields = ('user__first_name', 'user__last_name', 'note')
    # autocomplete_fields = ()
