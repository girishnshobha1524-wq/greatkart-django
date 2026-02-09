from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounts

# Custom admin configuration for Accounts model
class AccountAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    # Fields that are clickable links in the list view
    list_display_links = ('email', 'first_name', 'last_name')
    # Fields that cannot be edited in the admin
    readonly_fields = ('last_login', 'date_joined')
    # Default ordering of records (newest first)
    ordering = ('-date_joined',)
    
    # Remove default UserAdmin configurations that don't apply to our custom model
    filter_horizontal = ()  # No many-to-many fields to display horizontally
    list_filter = ()        # No filter options in sidebar
    fieldsets = ()          # Use default field grouping

# Register the Accounts model with custom admin configuration
admin.site.register(Accounts, AccountAdmin)