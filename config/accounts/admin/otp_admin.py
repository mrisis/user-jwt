from django.contrib import admin
from accounts.models import OTP


class OTPAdmin(admin.ModelAdmin):
    list_display = ['user', 'otp', 'timestamp']
    list_filter = ['timestamp']
    search_fields = ['user']
    ordering = ['-timestamp']
    readonly_fields = ['otp']

admin.site.register(OTP, OTPAdmin)