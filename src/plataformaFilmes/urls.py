from django.urls import path
from .views import index, filmes, registrar, excluir, detalhes, editar, atualizar


urlpatterns = [
    path("", index, name='index'),
    path("filmes", filmes, name='filme'),
    path("registrar", registrar, name='registrar'),
    path("detalhes/<int:id>", detalhes, name='detalhes'),
    path("editar/<int:id>", editar, name='editar'),
    path("atualizar/<int:id>", atualizar, name='atualizar'),
    path("excluir/<int:id>", excluir, name='excluir')
    
]
