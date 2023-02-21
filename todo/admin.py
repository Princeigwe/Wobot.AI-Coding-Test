from django.contrib import admin
from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_filter = ('name', 'description')
    list_display = ('name', 'description')

admin.site.register(Todo, TodoAdmin)