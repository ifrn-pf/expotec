# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from eventos.models import Usuario, Inscricao


@python_2_unicode_compatible
class AreaTema(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'área'
        verbose_name_plural = 'áreas'
        ordering = ('nome',)


@python_2_unicode_compatible
class Modalidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


@python_2_unicode_compatible
class Trabalho(models.Model):
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE,
                                   related_name='trabalhos')
    area = models.ForeignKey(AreaTema, on_delete=models.CASCADE,
                             related_name='trabalhos',
                             verbose_name='área')
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE,
                                  related_name='trabalhos')
    titulo = models.CharField(max_length=300)
    arquivo = models.FileField(upload_to='trabalhos', blank=False)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('titulo',)
