from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'data_joined', 'last_login', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('email', 'username',)
    readonly_fields = ('data_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)