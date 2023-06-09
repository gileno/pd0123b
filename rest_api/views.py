import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny

from eventos.models import Categoria, Evento

from rest_api.serializers import CategoriaSerializer, EventoSerializer


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
        serializer = CategoriaSerializer(instance=categorias, many=True)
        return Response({
            'resultados': serializer.data
        })

# Listagem de Categorias - GET (filtros) /api/categorias/ - list
# Criar Categorias - POST /api/categorias/ - create
# Visualizar uma Categoria - GET <id> /api/categorias/1/ - retrieve
# Atualizar uma Categoria - PUT<completa>/PATCH<parcial> <id> /api/categorias/1/ - update / update_partial
# Apagar uma Categoria - DELETE <id> /api/categorias/1/ - destroy
# Listagem de eventos de uma categoria - GET /api/categorias/1/eventos/ - eventos

# class CategoriaModelViewSet(ModelViewSet)
class CategoriaModelViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update', 'create']:
            return [IsAdminUser()]
        return [AllowAny()]

    @action(detail=True, methods=['GET'])
    def eventos(self, request, pk):
        # categoria = Categoria.objects.get(id=pk)
        categoria = self.get_object()
        eventos = Evento.objects.filter(categoria=categoria)
        serializer = EventoSerializer(instance=eventos, many=True)
        return Response(data=serializer.data)


class EventoModelViewSet(viewsets.ModelViewSet):

    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['categoria', 'destaque']

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update', 'create']:
            return [IsAdminUser()]
        return [AllowAny()]

    @action(detail=False, methods=['GET'])
    def destaques(self, request):
        eventos = Evento.objects.filter(destaque=True)
        serializer = EventoSerializer(instance=eventos, many=True)
        return Response(data=serializer.data)
