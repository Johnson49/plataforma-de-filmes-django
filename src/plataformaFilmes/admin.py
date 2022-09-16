from django.contrib import admin

from .models import Filme, Avaliacao

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano_lancamento", "duracao", "criacao", "ativo")



@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('filme', 'nome', 'email', 'avaliacao', 'ativo')