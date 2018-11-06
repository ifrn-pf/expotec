# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.conf import settings
from crispy_forms.helper import FormHelper
from eventos.models import Evento
from .utils.file_upload import UploadMaxSizeMixin, humanbytes
from .models import Trabalho


class SubmeterTrabalhoForm(UploadMaxSizeMixin, forms.ModelForm):
    arquivo = forms.FileField(
        help_text='Tamanho maximo de %s' % humanbytes(
            settings.FILE_UPLOAD_MAX_SIZE))
    helper = FormHelper()
    helper.form_tag = False

    evento = forms.ModelChoiceField(
        queryset=Evento.objects.filter(permite_trabalhos=True))

    class Meta:
        model = Trabalho
        fields = ('evento', 'titulo', 'modalidade', 'area', 'arquivo')
