# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import (MeusDadosView, ParticipanteView,
                    evento_inscrever, evento_desinscrever)

urlpatterns = [
    url(r'^inscrever-se/(?P<pk>\d+)$', evento_inscrever,
        name='eventos_inscrever_evento'),
    url(r'^desinscrever-se/(?P<pk>\d+)$', evento_desinscrever,
        name='eventos_desinscrever_evento'),
    url(r'^meus-dados$', MeusDadosView.as_view(),
        name='eventos_dados_usuario'),
    url(r'^$', ParticipanteView.as_view(),
        name='eventos_area_usuario'),
]
