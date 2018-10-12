# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import AreaTema, Modalidade, Trabalho


@admin.register(AreaTema)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Trabalho)
class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'inscricao', 'area', 'modalidade')
    list_filter = ('area', 'modalidade')
    search_fields = ('titulo',)
    raw_id_fields = ('inscricao',)
