from django.contrib import admin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name', 'email')

admin.site.register(CustomUser, CustomUserAdmin)