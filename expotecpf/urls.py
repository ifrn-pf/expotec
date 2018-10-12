from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from eventos.views import staticpage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^eventos/', include('eventos.urls')),
    url(r'^trabalhos/', include('trabalhos.urls')),
    url(r'', staticpage, name='home')
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            serve, {'document_root': settings.MEDIA_ROOT})
    ]
