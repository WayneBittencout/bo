from django.urls import path
from . import views

urlpatterns = [
    path('<int:ano>', views.index, name='index'),
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('lista/', views.BoLista.as_view(), name='lista-bo'),
    path('editar/<int:pk>', views.BoAtualizar.as_view(), name='editar-bo'),
    path('envolvido/', views.cadastro, name='envolvido'),
    path('envolvido/<int:pk>', views.EnvolvidoAtualizar.as_view(), name='envolvido-editar'),
    path('alerta/', views.alertas, name='alerta'),
    path('graficos/', views.graficos, name='graficos'),
 ]