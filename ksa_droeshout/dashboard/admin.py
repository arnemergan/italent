from django.contrib import admin

# Register your models here.
from .models import Groep,leiding


@admin.register(Groep)
class GroepAdmin(admin.ModelAdmin):
    pass

@admin.register(leiding)
class leidingAdmin(admin.ModelAdmin):
    pass