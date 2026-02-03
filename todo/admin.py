from django.contrib import admin

from . import models


@admin.register(models.Todo)
class Todoadmin(admin.ModelAdmin):
    list_display = ('title', 'status_colored', 'is_done', 'priority', 'created_at', 'updated_at', 'due_date')
    list_filter = ('is_done', 'priority', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_done',)
    ordering = ('-created_at',)
    