from django.contrib import admin
from .models import UserRegistration, AlertHistory

@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email1', 'created_at')

@admin.register(AlertHistory)
class AlertHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')
    list_select_related = ('user',)

# Register your models here.
