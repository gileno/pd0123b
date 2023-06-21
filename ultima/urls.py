from django.contrib import admin
from django.urls import path

from eventos.views import inicio, inscricao, categoria


urlpatterns = [
    path('', inicio, name='inicio'),
    path('categorias/<int:id>/', categoria, name='categoria'),
    path('inscricao/', inscricao, name='inscricao'),
    path('admin/', admin.site.urls),
]
