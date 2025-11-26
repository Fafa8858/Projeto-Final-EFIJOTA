from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('carrinho/', views.clientes, name='carrinho'),
    path('atualizar/', views.atualizar_cliente, name='atualizar_cliente'),
    path('excluir/', views.excluir_cliente, name='excluir_cliente'),

    # NOVA ROTA — página de sucesso do cliente
    path('compra/efetuada/', views.compra_efetuada_view, name='compra_efetuada'),

    # Contatos
    path('contato/', views.formulario_contato_view, name='contatos'),
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
]
