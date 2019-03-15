from django.contrib import admin
from .models import AgendaItem

@admin.register(AgendaItem)
class AgendaItemAdmin(admin.ModelAdmin):
    pass