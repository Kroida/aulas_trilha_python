from django.contrib import admin
from .models import Fruta

# Register your models here.

@admin.register(Fruta)
class FrutaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade', 'data_cadastro')
    search_fields = ('nome',)
    list_filter = ('data_cadastro',)
