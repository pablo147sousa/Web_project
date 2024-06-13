# artigos/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'artigos'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('info/<int:article_id>/', views.article_view, name='article'),
    path('autor/<int:autor_id>', views.autor_view, name='autor'),
    # Manipulação Autores
    path('autor/novo', views.new_author_view, name="novo_autor"),
    path('autor/<int:autor_id>/edita', views.edita_autor_view,name="edita_autor"),
    path('autor/<int:autor_id>/apaga', views.apaga_autor_view,name="apaga_autor"),
    # Manipulação Artigos
    path('autor/<int:autor_id>/adiciona', views.novo_artigo_view,name="novo_artigo"),
    path('info/<int:article_id>/edita', views.edit_article_view, name='edita_artigo'),
    path('info/<int:article_id>/apaga', views.apaga_artigo_view,name="apaga_artigo"),
    # Interações 
    path('artigo/<int:artigo_id>/comentar/', views.comment_article, name='comentar_artigo'),
    path('artigo/<int:artigo_id>/avaliar/', views.rate_article, name='avaliar_artigo'),
]