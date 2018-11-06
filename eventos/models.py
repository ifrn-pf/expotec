# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.formats import date_format, time_format, number_format


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Usuário deve ter endereço de e-mail')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password=password, **kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


@python_2_unicode_compatible
class Usuario(PermissionsMixin, AbstractBaseUser):
    nome_completo = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField('e-mail', unique=True, blank=False, null=False)
    cpf = models.CharField(unique=True, max_length=50,
                           blank=True, null=True,
                           verbose_name='CPF / Passaporte')
    endereco = models.CharField(max_length=500, blank=True, null=True,
                                verbose_name='endereço')
    cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    instituicao = models.CharField('instituição', max_length=100,
                                   blank=True, null=True)
    curso = models.CharField('curso', max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='ativo')
    date_joined = models.DateTimeField(default=timezone.now, editable=False,
                                       verbose_name='cadastro em')

    objects = UsuarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo']

    @property
    def username(self):
        return self.get_short_name()

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        if self.nome_completo:
            return self.nome_completo
        return self.get_short_name()

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        if self.nome_social:
            return self.nome_social
        return self.nome_completo

    class Meta:
        ordering = ('nome_completo', 'instituicao', 'curso')


@python_2_unicode_compatible
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    permite_trabalhos = models.BooleanField(
        default=False, verbose_name='permitir submissão de trabalhos')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


@python_2_unicode_compatible
class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE,
                               related_name='inscricoes')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,
                                related_name="inscricoes")

    def __str__(self):
        return '#%d' % (self.pk)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
