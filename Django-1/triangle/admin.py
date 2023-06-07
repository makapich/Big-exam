from django.contrib import admin

from .models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'timestamp', )
    search_fields = ('path',)
    list_filter = ('timestamp', 'method', )
    date_hierarchy = 'timestamp'
    list_per_page = 10
    ordering = ('-timestamp',)
    list_editable = ('method', )
    readonly_fields = ('timestamp',)
