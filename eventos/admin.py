# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UsuarioForm, UsuarioAddform
from .models import Usuario, Evento, Inscricao


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('nome_completo', 'email', 'instituicao', 'curso')
    list_filter = ('is_active', 'groups')
    search_fields = ('nome_completo', 'email', 'instituicao', 'curso')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
            'nome_completo', 'nome_social', 'cpf', 'endereco', 'cidade',
            'uf', 'pais', 'instituicao', 'curso'
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
            'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome_completo', 'email', 'password1', 'password2'),
        }),
    )
    form = UsuarioForm
    add_form = UsuarioAddform
    ordering = ('nome_completo',)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'usuario')
    raw_id_fields = ('usuario',)
