# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import SubmeterTrabalho

urlpatterns = [
    url(r'^submeter/(?P<evento>\d+)$', SubmeterTrabalho.as_view(),
        name='trabalhos_submeter_trabalho'),
    url(r'^submeter$', SubmeterTrabalho.as_view(),
        name='trabalhos_submeter_trabalho'),
]
