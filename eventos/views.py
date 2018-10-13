# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import (Http404, redirect,
                              get_object_or_404)
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from sfp.views import staticflatpage
from trabalhos.models import Trabalho
from .models import Usuario, Evento, Inscricao
from .forms import UsuarioChangeForm


def staticpage(request):
    return staticflatpage(request, request.path_info)


class MeusDadosView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioChangeForm

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        else:
            raise Http404

    def get_success_url(self):
        messages.success(self.request, 'Dados atualizados com successo.')
        return reverse('eventos_dados_usuario')


class ParticipanteView(LoginRequiredMixin, TemplateView):
    template_name = 'area-participante.html'

    def get_context_data(self, **kwargs):
        eventos = Evento.objects.all()
        for evento in eventos:
            evento.minha_inscricao = evento.inscricoes.filter(
                usuario=self.request.user).first()
            evento.meus_trabalhos = Trabalho.objects.filter(
                inscricao=evento.minha_inscricao)

        return {'eventos': eventos}


@login_required
def evento_inscrever(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    inscricao = Inscricao(usuario=request.user, evento=evento)
    inscricao.save()
    messages.success(request, 'Inscrição realizada com successo.')
    return redirect(reverse('eventos_area_usuario'))


@login_required
def evento_desinscrever(request, pk):
    Inscricao.objects.filter(
        usuario=request.user, evento_id=pk).delete()
    messages.success(request, 'Inscrição removida com successo.')
    return redirect(reverse('eventos_area_usuario'))
