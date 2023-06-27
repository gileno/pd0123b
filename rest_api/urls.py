from django.urls import path

from rest_api.views import categorias, api_inicio


app_name = 'rest_api'


urlpatterns = [
    path('', api_inicio, name='api_inicio'),
    path('categorias/', categorias, name='categorias'),
]
