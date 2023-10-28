from django.contrib import admin
from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone')
    search_fields = ('fullname', 'phone')
    list_filter = ('fullname', 'phone')
    ordering = ('fullname',)
    list_per_page = 25

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('fullname',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password'),
        }),
    )
    readonly_fields = ('password',)


admin.site.register(User, UserAdmin)

