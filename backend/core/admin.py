from django.contrib import admin
from .models import ErrorLog


@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ("method", "path", "status_code", "timestamp")
    search_fields = ("method", "path", "status_code")
