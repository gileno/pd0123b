import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view

from eventos.models import Categoria


# @csrf_exempt
# def api_inicio(request):
#     categoria = {
#         "id": 1,
#         "nome": "teste",
#     }
#     return HttpResponse(json.dumps(categoria))

@api_view(['GET'])
def api_inicio(request):
    categoria = {
        "id": 1,
        "nome": "teste",
    }
    return Response(categoria)


@api_view(['GET', 'POST'])
def categorias(request):
    if request.method == 'POST':
        dados = request.data
        nome = dados['nome']
        categoria = Categoria.objects.create(nome=nome)
        return Response({
            'id': categoria.id,
            'nome': categoria.nome,
            'criado_em': categoria.criado_em,
            'modificado_em': categoria.modificado_em,
        })
    else:
        categorias = Categoria.objects.all()
        resultados = []
        for categoria in categorias:
            resultados.append({
                'id': categoria.id,
                'nome': categoria.nome,
                'criado_em': categoria.criado_em,
                'modificado_em': categoria.modificado_em,
            })
        return Response({
            'resultados': resultados
        })

