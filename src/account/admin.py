from django.contrib import admin

from .models import Account


@admin.register(Account)
class ClientUserAdmin(admin.ModelAdmin):
    '''user management config'''
    list_display = ['username', 'email', 'phone_number', 'address', 'date_joined', 'is_active', 'first_name',
                    'last_name']
    list_filter = ['username', 'is_active', 'address', 'phone_number']
    list_editable = ['is_active']
