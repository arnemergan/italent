from django.contrib import admin
from verhuur import models
@admin.register(models.Lokaal)
class LokaalAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Tent)
class TentAdmin(admin.ModelAdmin):
    pass
@admin.register(models.TentFoto)
class TentFotoAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Lokaalfoto)
class LokaalFotoAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Weekend)
class WeekendAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Materiaal)
class MateriaalAdmin(admin.ModelAdmin):
    pass

