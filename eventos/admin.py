# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .forms import UsuarioForm
from .models import Usuario, Evento, Inscricao


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'instituicao', 'curso')
    search_fields = ('nome_completo', 'email', 'instituicao', 'curso')
    form = UsuarioForm


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'usuario')
    raw_id_fields = ('usuario',)
