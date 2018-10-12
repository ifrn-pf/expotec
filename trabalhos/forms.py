# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from .models import Trabalho
from eventos.models import Evento


class SubmeterTrabalhoForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    evento = forms.ModelChoiceField(
        queryset=Evento.objects.filter(permite_trabalhos=True))

    class Meta:
        model = Trabalho
        fields = ('evento', 'titulo', 'modalidade', 'area', 'arquivo')
