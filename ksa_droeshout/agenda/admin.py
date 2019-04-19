from django.contrib import admin
from .models import AgendaItem,Adres

@admin.register(AgendaItem)
class AgendaItemAdmin(admin.ModelAdmin):
    pass
@admin.register(Adres)
class AdresAdmin(admin.ModelAdmin):
    pass

