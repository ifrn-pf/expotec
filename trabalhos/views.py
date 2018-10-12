# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib import messages
from crispy_forms.helper import FormHelper
from eventos.models import Inscricao, Evento
from .forms import SubmeterTrabalhoForm
from .models import Trabalho


class SubmeterTrabalho(CreateView):
    model = Trabalho
    form_class = SubmeterTrabalhoForm
    success_url = reverse_lazy('eventos_area_usuario')

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
