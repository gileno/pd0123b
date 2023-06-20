import datetime as dt

from django.http import HttpResponse
from django.shortcuts import render

from eventos.models import Inscricao
from eventos.forms import InscricaoForm


def inicio(request):
    eventos = []
    eventos.append({
        'nome': 'Time A x Time B',
        'categoria': 'Esportivo',
        'data': 'Mai 30',
        'descricao': 'Jogo será no estádio lotado',
    })
    eventos.append({
        'nome': 'Show bem legal',
        'categoria': 'Shows',
        'data': 'Mai 31',
        'descricao': 'Show será interessante',
    })
    contexto = {
        'ano': dt.datetime.now().year,
        'categorias': ['Esportivo', 'Shows', 'Outros'],
        'eventos': eventos,
    }
    return render(request, 'inicio.html', contexto)


def inscricao(request):
    contexto = {
        'categorias': ['Esportivo', 'Shows', 'Outros'],
    }
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            contexto['sucesso'] = True
    else:
        form = InscricaoForm()
    contexto['form'] = form
    return render(request, 'inscricao.html', contexto)
