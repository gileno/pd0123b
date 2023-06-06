from django.contrib import admin
from django.urls import path

from eventos.views import inicio, inscricao


urlpatterns = [
    path('', inicio, name='inicio'),
    path('inscricao/', inscricao, name='inscricao'),
    path('admin/', admin.site.urls),
]
