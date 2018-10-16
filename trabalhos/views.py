# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings
from django.db.models import Count
from crispy_forms.helper import FormHelper
from eventos.models import Inscricao, Evento
from .forms import SubmeterTrabalhoForm
from .models import Trabalho


class SubmeterTrabalho(LoginRequiredMixin, CreateView):
    model = Trabalho
    form_class = SubmeterTrabalhoForm
    success_url = reverse_lazy('eventos_area_usuario')

    def get_form(self, *args, **kwargs):
        trabalhos_por_inscricao = getattr(settings, 'TRABALHOS_POR_INSCRICAO')
        form = super(SubmeterTrabalho, self).get_form(*args, **kwargs)
        eventos = Inscricao.objects.annotate(
            total_trabalhos=Count('trabalhos')).filter(
                usuario=self.request.user,
                evento__permite_trabalhos=True,
                total_trabalhos__lt=trabalhos_por_inscricao
                ).values_list('evento', flat=True)
        form.fields['evento'].queryset = Evento.objects.filter(pk__in=eventos)
        return form

    def get_context_data(self, **kwargs):
        helper = FormHelper()
        helper.form_tag = False
        kwargs['form_helper'] = helper
        return super(SubmeterTrabalho, self).get_context_data(**kwargs)

    def get_initial(self):
        evento_id = self.kwargs.get('evento', None)
        if evento_id:
            evento = get_object_or_404(Evento, pk=evento_id)
            return {'evento': evento}
        return {}

    def form_valid(self, form):
        evento = form.cleaned_data.get('evento')
        inscricao = get_object_or_404(Inscricao, usuario=self.request.user,
                                      evento=evento)
        form.instance.inscricao = inscricao
        messages.success(self.request, 'Trabalho submetido com sucesso.')
        return super(SubmeterTrabalho, self).form_valid(form)
