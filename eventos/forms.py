# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (ReadOnlyPasswordHashField,
                                       UserCreationForm)
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from .models import Usuario, Evento, Inscricao


class UsuarioForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password/\">this form</a>."
        ),
    )

    class Meta:
        model = Usuario
        fields = ('nome_completo', 'nome_social', 'email', 'cpf',
                  'endereco', 'cidade', 'uf', 'pais',
                  'instituicao', 'curso', 'is_staff', 'groups')


class UsuarioAddform(UserCreationForm):
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.email = self.cleaned_data.get('email')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2


class UsuarioChangeForm(UsuarioForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioChangeForm, self).__init__(*args, **kwargs)
        for f in ('cpf', 'endereco', 'cidade', 'uf', 'pais'):
            self.fields[f].required = True


class RegisterForm(UsuarioForm):
    evento = forms.ModelMultipleChoiceField(
        queryset=Evento.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    password1 = forms.CharField(
        label='Senha',
        help_text='Use pelo menos 6 caracteres.',
        widget=forms.PasswordInput(),
        min_length=6)

    password2 = forms.CharField(
        label='Confirmar senha',
        help_text='Use pelo menos 6 caracteres.',
        min_length=6,
        widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for f in ('cpf', 'endereco', 'cidade', 'uf', 'pais'):
            self.fields[f].required = True

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password1 != password2:
            raise forms.ValidationError(
                'A senha e a confirmção devem ser iguais')

    def save(self, *args, **kwargs):
        usuario = super(RegisterForm, self).save(*args, **kwargs)
        usuario.set_password(self.cleaned_data['password1'])
        if kwargs.get('commit', True):
            usuario.save()
            for evento in self.cleaned_data.get('evento'):
                Inscricao(usuario=usuario, evento=evento).save()
        return usuario

    class Meta:
        model = Usuario
        fields = ('evento', 'nome_completo', 'nome_social', 'email', 'cpf',
                  'endereco', 'cidade', 'uf', 'pais',
                  'instituicao', 'curso', 'password1', 'password2')
