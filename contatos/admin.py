from django.contrib import admin
from .models import Categoria, Contato

# Register your models here.
admin.site.register(Categoria)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone')
    list_display_links = ('id', 'nome')
    list_per_page = 10
